# python script for flask to run our web page
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from jinja2 import Template

# web app
app = Flask(__name__, static_folder='./static')

@app.route('/')
def index():
    return render_template('home_page.html')


@app.route('/CH4')
def CH4():
    return render_template('home_page.html', tableau_file = 'CH4.html')


# start the server
if __name__ == '__main__':
    app.run(debug=True, port = 5000)

