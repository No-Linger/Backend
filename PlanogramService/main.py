from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
database = MongoClient(DATABASE_URL)["NoLinger"]
planogramCollection = database["Planograms"]

app = Flask("No Linger Planogram Service")
CORS(app)


@app.route("/getPlanograms")
def get_planograms():
    planograms = []
    response = planogramCollection.find({})
    for planogram in response:
        planogram["_id"] = str(planogram["_id"])
        planograms.append(planogram)
    return jsonify({"planograms": planograms}), 200


if __name__ == "__main__":
    app.run(port="8082", debug=True, host="0.0.0.0")
