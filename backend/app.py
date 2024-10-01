from flask import Flask, request, jsonify
from flask_cors import CORS
import pdb
import jwt
app = Flask(__name__)
CORS(app)
JWT_SECRET = 'code'

# def generateJWT(email, userId, jwt_secret):
#     payload = {
#         'email': email,
#         'user_id': userId,
#     }
#     token = jwt.encode(payload, jwt_secret, algorithm='HS256')
#     return token

# def decodeJWT(token, jwt_secret):
#     try:
#         decoded = jwt.decode(token, jwt_secret, algorithms=["HS256"])
#         user_id = decoded.get('user_id')
#         return user_id[0]
#     except jwt.ExpiredSignatureError:
#         print("The token has expired.")
#         return None
#     except jwt.InvalidTokenError:
#         print("Invalid token.")
#         return None

# # post register
# @app.route('/register', methods=['POST'])
# def registerNewUser():
#     try:
#         print('rtehee')
#         data = request.json
#         email = data['email']
#         password = data['password']
#         name = data['name']
#         print(email)
#         newUser = User(email, name, password)
#         return jsonify(token=generateJWT(email, newUser.id, JWT_SECRET))

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # login
# @app.route('/login', methods=['POST'])
# def login():
#     try:
#         data = request.json
#         email = data['email']
#         password = data['password']
#         print('here')
#         res = User.checkLogin(email, password)
#         if res is not None:
#             return jsonify(token=generateJWT(email, res, JWT_SECRET))
#         return jsonify({"error": str(e)}), 500

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
