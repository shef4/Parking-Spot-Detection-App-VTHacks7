import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from objectrecognition import *

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',method=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    image = [plt.imread(path) for path in glob.glob('test_images/*.jpg')]
    predicted_images = predict_on_image(image,final_spot_dict)
    output = predicted_images

    return render_template('index.html', prediction_text='there are $ {} empty spots'.format(output))

@app.route('/predict_api',method=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    predicted_images = predict_on_image(test_images,final_spot_dict)
    output = predicted_images

    return jsonify(output)