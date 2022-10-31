# From https://www.datacamp.com/tutorial/machine-learning-models-api-python
from flask import Flask, request, jsonify
import flask_monitoringdashboard as dashboard # docu en https://flask-monitoringdashboard.readthedocs.io/en/latest/configuration.html y https://flask-monitoringdashboard.readthedocs.io/en/latest/functionality.html
import pickle
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

dashboard.bind(app)
@app.route('/predict', methods=['POST'])
def predict():
    if rf:
        try:
            json_ = request.json
            query = pd.DataFrame(json_)
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(rf.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    rf = pickle.load(open('saved_models/model_01.pkl', 'rb')) # Load "model.pkl"
    print ('Model loaded')
    model_columns = pickle.load(open('saved_models/columns_01.pkl', 'rb')) # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)