from flask import Flask, jsonify, abort  
  
app = Flask(__name__)

@app.route('/api/v1/token/<key>', methods=['GET'])  
def token(key):  
	test_data = {  
		"e8990ab9be26": "3OX9+p39QLIvE6+x/w=",  
		"b01323031589": "wBvlo9G7Wqxsb2P9YS=",  
	}  
	secret = test_data.get(key)  
	if secret is None:  
		abort(404)  
	return jsonify({"key": key, "token": secret})