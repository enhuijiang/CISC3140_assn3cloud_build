from flask import Flask, render_template, request
import urllib.request
import json


app = Flask(__name__)

@app.route('/')
def main():
    apodurl = 'https://api.nasa.gov/planetary/apod?'
    key = 'IhPDteqpCVmrbDaRXp5bY820KvCUcxUhmeiRVexV'
    imgUrl = buildURL(apodurl, key)

    return render_template('home_page.html', imgUrl=imgUrl)

@app.route('/key', methods=['POST'])
def key():
    apodurl = 'https://api.nasa.gov/planetary/apod?'
    key = request.form['apikey']
    urlObj = urllib.request.urlopen(apodurl + 'api_key=' + key)
    read = urlObj.read()
    decode = json.loads(read.decode('utf-8'))
    imgUrl = decode['url']
    return render_template('home_page.html', imgUrl=imgUrl)

def buildURL(apodurl, key):
        urlObj = urllib.request.urlopen(apodurl + 'api_key=' + key)
        read = urlObj.read()
        decode = json.loads(read.decode('utf-8'))

        imgUrl = decode['url']
        return imgUrl

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)