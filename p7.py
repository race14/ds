
####server/api.py############

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = a + b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
    
  




######client.py#######
import requests

data = {
    'a': 10,
    'b': 20
}

response = requests.post('http://localhost:5000/add', json=data)
result = response.json()
print("Result of addition:", result['result'])

    



# In[ ]:




