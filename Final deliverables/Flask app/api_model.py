# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:13:21 2022

@author: HP
"""


from flask  import Flask, render_template,request
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('RF.sav','rb'))

@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict',methods =['GET','POST'])
def index():
    return render_template('Prediction.html')

@app.route('/data_predict', methods=['POST'])

def predict():
    
    form_values = request.form.to_dict()
    columns =["age","gender","tb","db","ap","aa1","aa2","tp","a","agr"]
    data = np.asarray([float(form_values[i].strip()) for i in columns]).reshape(1,-1)
    
    
    prediction =model.predict(data)[0]
    
    if(prediction == 1):
        return render_template('Output.html',prediction ='You have a liver disease and you must take treatment')
    else :
        return render_template('Output.html',prediction ='You do not have liver disease')
   

if __name__ =='__main__':
    app.run(debug=True)


















    
    
    
    
    
    
    