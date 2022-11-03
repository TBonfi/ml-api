


##############################################################################################
### ESTA VERSIÓN SI ES PARA EJECUTAR EN DEEEPNOTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE ###
##############################################################################################



# From https://www.datacamp.com/tutorial/machine-learning-models-api-python
from flask import Flask, request, jsonify
import flask_monitoringdashboard as dashboard # docu en https://flask-monitoringdashboard.readthedocs.io/en/latest/configuration.html y https://flask-monitoringdashboard.readthedocs.io/en/latest/functionality.html VER CONFIG EN https://github.com/flask-dashboard/Flask-MonitoringDashboard/blob/master/config.cfg
import pickle
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

dashboard.bind(app)
@app.route('/predict/v1/<model>', methods=['POST'])
def predict(model):
    
    model_columns = pickle.load(open('saved_models/columns_01.pkl', 'rb'))

    if model=='lr_01':
        
        lr = pickle.load(open('saved_models/lr_model_01.pkl', 'rb'))

        try:
            json_ = request.json
            query = pd.DataFrame(json_)
            query = query.reindex(columns=model_columns, fill_value=0)
            
            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction), 'model': 'lr_01'})

        except:

            return jsonify({'trace': traceback.format_exc()})

    elif model=='rf_01':
        
        rf = pickle.load(open('saved_models/rf_model_01.pkl', 'rb'))
            
        try:    
            json_ = request.json
            query = pd.DataFrame(json_)
            query = query.reindex(columns=model_columns, fill_value=0)
            
            prediction = list(rf.predict(query))

            return jsonify({'prediction': str(prediction), 'model': 'rf_01'})

        except:

            return jsonify({'trace': traceback.format_exc()})        
    else:

        return ('No model here to use')

@app.route('/bienvenida/<nombre>', methods=['POST', 'GET'])
def hello_not_really_stranger(nombre):
    return f"Hola {nombre}! viste que tremenda API?"

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)