from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
app.debug = True

@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
     query2 = list(query.columns.values)[:-1]
     prediction = clf.predict(query[query2])
     return jsonify({'prediction': list(prediction)})

@app.route('/hello')
def home():
   return "Hello World! R1"

if __name__ == '__main__':
     clf = joblib.load('model/finalized_model.pkl')
     model_columns = joblib.load('model/finalized_model_column.pkl')
     app.run(host='0.0.0.0', port=8080)