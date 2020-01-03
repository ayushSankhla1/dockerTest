from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Welcome(Resource):
	@staticmethod
	def post():
		posted_data = request.get_json()
		name = posted_data['name']
		print(name)
		type(name)
		returnText = "Hello "+ str(name)
		return jsonify({
			'return': name
		})


api.add_resource(Welcome, '/welcome')
if __name__ == '__main__':
	app.run(debug=True)

