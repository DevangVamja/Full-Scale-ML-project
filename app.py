from flask import Flask, request, render_template, jsonify
from src.exception import CustomException
from src.logger import logging
from src.pipeline.test_pipeline import CustomData, Prediction
from src.pipeline.train_pipeline import TrainPipeline
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def Train():
    try:
        new_TP = TrainPipeline()
        final_accuracy = new_TP.initiate_train_pipeline()
    except CustomException as e:
        logging.error(e)
    return render_template('train.html', accuracy=round(final_accuracy*100,2))

@app.route('/predict', methods=['GET','POST'])
def Predictions():
    if request.method == 'POST':
        request_data = CustomData(request.form).to_df()
        pred = Prediction(request_data).predicts()
        print(pred)    
        return jsonify({'maths_score': pred[0]})
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)