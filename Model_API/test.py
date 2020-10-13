import requests

url = "http://localhost:8080/predict"
datas = {"preg":[6],"plas":[148],"pres":[72],"skin":[35],"test":[0],"mass":[33.6],"pedi":[0.627],"age":[50],"class":[0]}
headers = {'Content-type': 'application/json'}
rsp = requests.post(url, json=datas, headers=headers)
print(rsp)
print(rsp.text)