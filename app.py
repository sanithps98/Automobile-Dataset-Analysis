# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:23:24 2021

@author: Acer
"""
from flask import Flask, render_template, request , jsonify
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from joblib import load

app = Flask(__name__)
app.config['SECRET_KEY']='mukul'

@app.route('/',methods=['GET'])
def Home():
    return render_template('mainpafe.html')



standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Highway_mpg=float(request.form['milage'])
        engine_size=int(request.form['size_of_the_engine'])
        curb_weight=int(request.form['weight_of_a_car'])
        horse_power=int(request.form['power'])
        model =load('model_final.joblib')
        prediction=model.predict([[Highway_mpg,engine_size,curb_weight,horse_power]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('mainpafe.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('mainpafe.html',prediction_text="You Can Sell The Car at ${}".format(output))
    else:
        return render_template('mainpafe.html')

if __name__=="__main__":
    app.run()