# pip install flask

from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np
import os
# loading the label encoder 
encoder=pickle.load(open('label_encoder.pkl','rb'))

# loading my mlr model
model=pickle.load(open("model.pkl",'rb'))

#loading Scaler
scalar=pickle.load(open("scaler.pkl",'rb'))

# Flask is used for creating your application
# render template is use for rendering the html page


app= Flask(__name__)  # your application


@app.route('/')  # default route 
def home():
    return render_template('home.html') # rendering if your home page.

@app.route('/pred',methods=['POST']) # prediction route
def predict1():
    a1=request.form["age"]
    a2=request.form["time_in_hospital"]
    a3=request.form["num_lab_procedures"]
    a4=request.form["num_procedures"]
    a5=request.form["num_medications"]
    a6=request.form["number_outpatient"]
    a7=request.form["number_emergency"]
    a8=request.form["number_inpatient"]
    a44=request.form["number_diagnoses"]
    a9=request.form["race"]
    a10=request.form["gender"]
    a11=request.form["admission_type_id"]
    a12=request.form["discharge_disposition_id"]
    a13=request.form["admission_source_id"]
    a14=request.form["diag_1"]
    a15=request.form["diag_2"]
    a16=request.form["diag_3"]
    a17=request.form["max_glu_serum"]
    a18=request.form["A1Cresult"]
    a19=request.form["metformin"]
    a20=request.form["repaglinide"]
    a21=request.form["nateglinide"]
    a22=request.form["chlorpropamide"]
    a23=request.form["glimepiride"]
    a24=request.form["acetohexamide"]
    a25=request.form["glipizide"]
    a26=request.form["glyburide"]
    a27=request.form["tolbutamide"]
    a28=request.form["pioglitazone"]
    a29=request.form["rosiglitazone"]
    a30=request.form["acarbose"]
    a31=request.form["miglitol"]
    a32=request.form["troglitazone"]
    a33=request.form["tolazamide"]
    a34=request.form["examide"]
    a35=request.form["citoglipton"]
    a36=request.form["insulin"]
    a37=request.form["glyburide-metformin"]
    a38=request.form["glipizide-metformin"]
    a39=request.form["glimepiride-pioglitazone"]
    a40=request.form["metformin-rosiglitazone"]
    a41=request.form["metformin-pioglitazone"]
    a42=request.form["change"]
    a43=request.form["diabetes_med"]
    t =  [a1,a2,a3,a4,a5,a6,a7,a8,a44,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43]
    
    for i in range(0,len(t)):
        t[i]=float(t[i])
    
    t=np.reshape(t,[1,-1])
    output =model.predict(t)
    print(output)
    if output==0:
        return render_template("home.html", result = "You Have to not admit")
    else:
        return render_template("home.html", result = "The have to readmit")

    
    
    
    
    
# running your application
if __name__ == "__main__":
    app.run()

#http://localhost:5000/ or localhost:5000
