from flask import Flask, request, render_template, json, jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hugo Boss ML'

@app.route('/',methods=['POST'])
def predict():
    body = request.get_json()
    prediction = model.predict(np.array([[body['productId'],body['factoryId'],body['amount']]]))
    return jsonify({'productionTime': prediction[0][0]})

if __name__  == '__main__':
    model = pickle.load(open('model.pkl','rb'))
    app.run(debug=True, host='0.0.0.0')