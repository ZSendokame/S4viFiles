import os
from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.errorhandler(404)
def notFound(status):
    return render_template('404.html', path=request.path)

@app.get('/')
def root():
    fileList = os.listdir('./files')

    return render_template(
        'index.html',
        fileLenght=len(fileList),
        file=fileList
    )

@app.get('/readme.md')
def readme():
    return render_template('readme.html')

@app.get('/view/<filename>')
def returnFile(filename):
    return send_file('./files//' + filename)

app.run()
