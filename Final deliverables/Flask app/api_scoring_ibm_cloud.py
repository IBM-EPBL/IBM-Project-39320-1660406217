import requests

import flask
from flask import render_template,request
from flask_cors import CORS

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "mEN1R-IypcevD8OJ3TmLAuEF69C53deaLliQClu7Qg-m"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = flask.Flask(__name__,static_url_path='')
CORS(app)

@app.route('/',methods =['GET','POST'])
def home():
    return render_template('Home.html')


@app.route('/predict',methods =['GET','POST'])
def index():
    return render_template('Prediction.html')

@app.route('/data_predict', methods=['POST'])

def predict():
    age =float(request.form['age'])
    gender =float(request.form['gender'])
    tb =float(request.form['tb'])
    db =float(request.form['db'])
    ap =float(request.form['ap'])
    aa1 =float(request.form['aa1'])
    aa2 =float(request.form['aa2'])
    tp =float(request.form['tp'])
    a =float(request.form['a'])
    agr =float(request.form['agr'])
    
    X=[[age,gender,tb,db,ap,aa1,aa2,tp,a,agr]]

# NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [['age','gender','tb','db','ap','aa1','aa2','tp','a','agr']], "values": X}]}
    
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/58fa0711-e9d9-4847-adca-ce45c5a43f93/predictions?version=2022-11-18', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    predictions = response_scoring.json()
    predict = predictions['predictions'][0]['values'][0][0]
    if(predict == 1):
        return render_template('Output.html',prediction ='You have a liver disease and you must take treatment')
    else :
        return render_template('Output.html',prediction ='You have dont have liver')
   

if __name__ =='__main__':
    app.run(debug=True)

