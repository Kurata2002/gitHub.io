from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def get_user_data():
    co2 = round(random.uniform(400, 2000), 2)
    aqi = random.randint(1, 5)
    tvoc = round(random.uniform(0, 6500), 2)
    return {'CO2': co2, 'AQI': aqi, 'TVOC': tvoc}

@app.route('/', methods=['GET'])
def get_user():
    user_data = get_user_data()
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(port=3000)
