from app import app
from flask import request, jsonify
from flask_cors import CORS
from db import Database
from config import Config
from app.models.planograms import Planograms

CORS(app)

database = Database(url=Config.DATABSE_URL, databaseName=Config.DATABASE_NAME)

database.connect()

@app.route('/createPlanogram', methods = ["POST"])
def insert_planogram():
    """
    Inserts a planogram into the MongoDB collection.

    Args:
        `name`: The name of the planogram

        `store`: The store where the planogram is assigned

        `date`: The date of the planogram is uploaded

        `img`: The image of the planogram

    Returns:
        A JSON response with a success message and a status code of 200 if the planogram is inserted successfully.
        A JSON response with an error message and a status code of 500 if an error occurs during the insertion process.
    """
    try:
        planogram = request.json

        planogram = Planograms(
            name=planogram["name"],
            store=planogram["store"],
            date=planogram["date"],
            img=planogram["img"],
            collection=database.get_collection("Planograms")
        )

        planogram.insert()
        return jsonify({"message": "Planogram inserted successfully!"}), 200

    except Exception as e: 
        print(str(e))
        return jsonify({"message": "Error inserting planogram!"}), 500
