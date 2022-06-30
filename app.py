from flask import Flask, render_template, request
import os.path
import nltk
import re
from operator import itemgetter


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


@app.route('/filter1', methods=['POST', 'GET'])
def filter1():
    number = int(request.form["number"])
    f = open("Grimm.txt", "r", errors='ignore')
    data_file = f.read()
    sentences = nltk.sent_tokenize(data_file)
    for i in range(len(sentences)):
        sentences[i] = sentences[i].split(' ', 1)[1]
        sentences[i] = re.sub(r'[^\w\s]+', ' ', sentences[i])
        tokens = nltk.word_tokenize(sentences[i])
        for word in tokens:
            if word.isupper():
                if word not in testdict:
                    testdict[word] = 1
                else:
                    testdict[word] = testdict[word]+1
    res = dict(sorted(testdict.items(),
               key=itemgetter(1), reverse=True)[:number])
    return render_template('1.html', data=res, len=len(res))


@app.route('/send', methods=['POST', 'GET'])
def send():
    searchtext = request.form['searchtext']
    searchTextFirst = searchtext.split(" ")[0]
    msg = "Search results for "+searchtext
    lst = []
    if searchTextFirst in dict:
        first = dict[searchTextFirst]
        for value in first:
            if searchtext in value['sentence']:
                lst.append(value)
    print(lst)
    return render_template('2.html', msg=msg, lst=lst)


if __name__ == '__main__':
    app.run()
