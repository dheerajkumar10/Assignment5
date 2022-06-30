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


testdict = {}
list = []
with open('./SpanishStopWords.txt', 'r') as f1:
    stopWords = f1.readlines()
    stopWords = [i.strip() for i in stopWords]


@app.route('/filter1', methods=['POST', 'GET'])
def filter1():
    with open('./Alamo.txt', 'r', encoding="utf8") as file:
        sentences = file.readlines()
        for i in range(len(sentences)):
            tokens = nltk.word_tokenize(sentences[i])
            for word in tokens:
                if word in stopWords:
                    if word not in testdict:
                        testdict[word] = 1
                    else:
                        testdict[word] = testdict[word]+1
    return render_template('1.html', data=testdict)


@app.route('/filter2', methods=['POST', 'GET'])
def filter2():
    rtxt = request.form['rtxt']
    rtxt1 = request.form['rtxt1']
    f = open("Akamo.txt", "r")
    data_file = f.read()

    sentences = nltk.sent_tokenize(data_file)

    filedata = filedata.replace(rtxt, rtxt1)
    with open('Grimm.txt', 'w') as file:
        file.write('filedata.txt', 'r')
    f = open("Grimm.txt", "r", errors='ignore')
    data_file = f.read()
    sentences = nltk.sent_tokenize(data_file)
    for i in range(len(sentences)):
        tokens = nltk.word_tokenize(sentences[i])
        for word in tokens:
            if(word == rtxt1):
                list.append(sentences[i])
    new_list = list[:8]
    return render_template('2.html', lst=new_list, len=range(new_list))


if __name__ == '__main__':
    app.run()
