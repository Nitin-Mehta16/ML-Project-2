from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline,CustomData

application = Flask(__name__)
app=application
 
## Route for home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == "GET":
         return render_template('predict.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')),
            )
        df_of_data=data.convert_data_as_data_frame()
        print(df_of_data)
        predict_pipeline=PredictPipeline()
        result=predict_pipeline.predict(df_of_data)
        return render_template('predict.html',result=result[0])
    
if __name__ == '__main__':
    app.run (host="0.0.0.0", debug=True)

        