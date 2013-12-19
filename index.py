# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import tasks

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def form():
    if request.method == 'POST':
        message = tasks.construct(request.files['image'])
        return message
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run()