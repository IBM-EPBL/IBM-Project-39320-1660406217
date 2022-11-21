import flask
from flask import render_template,request
from flask_cors import CORS
import joblib

app = flask.Flask(__name__,static_url_path='')
CORS(app)

@app.route('/')
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
    model = joblib.load('RF.sav')
    prediction =model.predict(X)[0]
   
    
    if(prediction == 1):
        return render_template('Output.html',prediction ='You have a liver disease and you must take treatment')
    else :
        return render_template('Output.html',prediction ='You have dont have liver')
   

if __name__ =='__main__':
    app.run(debug=True)


















    
    
    
    
    
    
    