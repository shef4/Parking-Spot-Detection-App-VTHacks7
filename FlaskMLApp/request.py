import request

url = 'http://localhost:5000/predict_api'
r = request.post(url,json={'image': A})

print(r.json())