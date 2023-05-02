# python script for flask to run our web page
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from jinja2 import Template

# web app
app = Flask(__name__, static_folder='./static')

@app.route('/')
def index():
    return render_template('home_page.html')


@app.route('/Kyoto')
def CH4():
    return render_template('home_page.html', tableau_file = 'Kyoto.html')

@app.route('/Basel')
def Basel():
    return render_template('home_page.html', tableau_file = 'Basel.html')

@app.route('/Desert')
def Desert():
    return render_template('home_page.html', tableau_file = 'Desert.html')

@app.route('/Heritage')
def Heritage():
    return render_template('home_page.html', tableau_file = 'Heritage.html')

@app.route('/Paris')
def Paris():
    return render_template('home_page.html', tableau_file = 'Paris.html')

@app.route('/UNFCCC')
def UNFCCC():
    return render_template('home_page.html', tableau_file = 'UNFCCC.html')
    
# start the server
if __name__ == '__main__':
    app.run(debug=True, port = 5000)

