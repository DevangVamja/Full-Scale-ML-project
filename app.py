from flask import Flask, request, render_template
from src.exception import CustomException
from src.logger import logging
from src.pipeline.test_pipeline import CustomData, Prediction
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET','POST'])
def Predictions():
    if request.method == 'POST':
        request_data = CustomData(request.form).to_df()
        pred = Prediction(request_data).predicts()
        print(pred)
        
        pass
    return render_template('train.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)