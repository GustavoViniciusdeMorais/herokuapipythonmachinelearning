import pickle
import numpy as np
from flask import Flask, request, jsonify

model = None
app = Flask(__name__)

def load_model():
    global model
    # model variable refers to the global variable
    with open('naive_bayes.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route('/')
def home_endpoint():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a json
        solids = data['Solids']
        chloramines = data['Chloramines']
        organic_carbon = data['Organic_carbon']
        data = np.array([solids, chloramines, organic_carbon])
        data = np.array(data)[np.newaxis, :]
        prediction = model.predict(data)
        return jsonify(str(prediction[0]))

if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(threaded=True, port=5000)
    #app.run(host='0.0.0.0', port=5000)
