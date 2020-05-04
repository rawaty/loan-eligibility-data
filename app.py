import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('loan.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features  = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    if output==0:
    	return render_template('index.html',prediction_text=" Opps You are Not Eligible for Loan:{}".format(math.floor(output)))
    else:
    	return render_template('index.html',prediction_text=" Congratulations You are Eligible for Loan:{}".format(math.floor(output)))

if __name__ == '__main__':
    app.run(debug=True)