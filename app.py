from cgi import test
from flask import Flask, render_template, request
import os.path
import nltk
import re
from operator import itemgetter
from nltk.tokenize import word_tokenize


app = Flask(__name__)
nltk.download('punkt')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/1')
def add():
    return render_template('1.html')


@app.route('/2')
def search():
    return render_template('2.html')


@app.route('/3')
def search1():
    return render_template('3.html')


list = []
with open('./SpanishStopWords.txt', 'r') as f1:
    stopWords = f1.readlines()
    stopWords = [i.strip() for i in stopWords]


@app.route('/filter1', methods=['POST', 'GET'])
def filter1():
    testdict = {}
    with open('./Alamo.txt', 'r', encoding="utf8") as file:
        data_file = file.read()
        sentences = nltk.sent_tokenize(data_file)
        for i in range(len(sentences)):
            tokens = nltk.word_tokenize(sentences[i])
            for word in tokens:
                if word in stopWords:
                    if word not in testdict:
                        testdict[word] = 1
                    else:
                        testdict[word] = testdict[word]+1
                    print(testdict[word])
    return render_template('1.html', data=testdict)


@app.route('/filter2', methods=['POST', 'GET'])
def filter2():
    rtxt = request.form['rtxt']
    rtxt1 = request.form['rtxt1']
    f = open("./Alamo.txt", "r", encoding="utf8")
    data_file = f.read()

    data_file = data_file.replace(rtxt, rtxt1)
    with open('./Alamo1.txt', 'w', encoding="utf8") as file:
        file.write(data_file)
    f1 = open("./Alamo1.txt", "r", errors='ignore', encoding="utf8")
    data_file1 = f1.read()
    sentences = nltk.sent_tokenize(data_file1)
    for i in range(len(sentences)):
        tokens = nltk.word_tokenize(sentences[i])
        for word in tokens:
            if(word == rtxt1):
                list.append(sentences[i])
    new_list = list[:5]
    return render_template('2.html', lst=new_list, len=len(new_list))


@app.route('/filter3', methods=['POST', 'GET'])
def filter3():
    testdict = {}
    number = request.form['number']
    f = open("./Alamo.txt", "r", errors='ignore', encoding="utf8")
    data_file = f.read()
    sentences = nltk.sent_tokenize(data_file)
    for i in range(len(sentences)):
        sentences[i] = re.sub(r'[^\w\s]+', ' ', sentences[i])
        pattern = r'[0-9]'
        sentences[i] = re.sub(pattern, '',  sentences[i])
        tokens = nltk.word_tokenize(sentences[i])
        for word in tokens:
            if word.isupper():
                if word not in testdict:
                    testdict[word] = 1
                else:
                    testdict[word] = testdict[word]+1
    res = dict(sorted(testdict.items(),
               key=itemgetter(1), reverse=True)[:number])
    return render_template('3.html', data=res)


if __name__ == '__main__':
    app.run()
