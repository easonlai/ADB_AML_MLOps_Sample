from flask import Flask, request, render_template
import requests


app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST']) 
def predict():
    if request.method == 'POST':
        url = "http://localhost_model_api_url:8080/predict"
        datas = {"preg":[request.values['preg']],"plas":[request.values['plas']],"pres":[request.values['pres']],"skin":[request.values['skin']],"test":[request.values['test']],"mass":[request.values['mass']],"pedi":[request.values['pedi']],"age":[request.values['age']],"class":[request.values['class']]}
        headers = {'Content-type': 'application/json'}
        rsp = requests.post(url, json=datas, headers=headers)

        return 'Prediction result is ' + rsp.text

    return render_template('index.html')

@app.route('/hello')
def home():
   return "Hello World! R1"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)