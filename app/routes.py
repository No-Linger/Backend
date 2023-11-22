import logging
from app import app
from flask import request, jsonify
from flask_cors import CORS
from db import Database
from config import Config
from app.models.planograms import Planograms
from app.models.statistics import Statistics
from app.models.stores import Stores
from app.models.users import Users

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
            img_path=planogram["img"],
            collection=database.get_collection("Planograms")
        )

        planogram.insert()
        return jsonify({"message": "Planogram inserted successfully!"}), 200

    except Exception as e: 
        print(str(e))
        return jsonify({"message": "Error inserting planogram!"}), 500

@app.route('/getPlanograms', methods = ["GET"])
def get_planogram():
    planograms = []

    response = database.get_collection("Planograms").find({})
    for planogram in response:
        planogram["_id"] = str(planogram["_id"])
        planograms.append(planogram)
    
    return jsonify({"planograms": planograms}), 200

@app.route('/saveStatistics', methods = ["POST"])
def insert_stats():
    try:
        data = request.json
        statistics = Statistics(
            date='',
            time='',
            model_percentage='',
            error_percentage='',
            collection=database.get_collection("Statistics")
        )
        
        statistics_list = []
        for item in data:
            statistic = statistics
            statistic.date = item["date"]
            statistic.time = item["time"]
            statistic.model_percentage = item['model_percentage']
            statistic.error_percentage = item['error_percentage']

            statistics_list.append(statistic.to_dic())

        statistics.insert_many(statistics_list)
        logging.info("Inserted data in db")
        return jsonify({"message": "Saved data!"}), 200
    except Exception as e:
        logging.exception(e)
        return jsonify({"error":"Error saving the data"}), 500
    
@app.route('/getStatistics', methods = ["GET"])
def get_stats():
    try:
        stats = []

        response = database.get_collection("Statistics").find({})
        for stat in response:
            stat["_id"] = str(stat["_id"])
            stats.append(stat)

        logging.info("Successfully retrieved data")
        return jsonify({"statistics": stats})
    except Exception as e:
       logging.exception(str(e))
       return jsonify({"error": "Error getting data from database"}) 

@app.route('/saveStore', methods = ["POST"])
def insert_store():
    try:
        data = request.json

        stores = Stores(
            name=data["name"],
            address=data["address"],
            manager=data["manager"],
            collection=database.get_collection("Stores")
        )

        stores.insert()
        logging.info("Inserted store data")

        return jsonify({"message": "Saved store data!"}), 200
    except Exception as e:
        logging.exception(str(e))

        return jsonify({"error": "Error saving store data"})

@app.route('/getStores', methods = ["GET"])
def get_stores():
    try:
        stores = []

        response = database.get_collection("Stores").find({})
        for store in response:
            store["_id"] = str(store["_id"])
            stores.append(store)

        logging.info("Successfully retrieved store data")
        return jsonify({"stores": stores})
    except Exception as e:
        logging.exception(str(e))
        return jsonify({"error": "Error getting store data from database"})
    
@app.route('/createUser',methods = ["POST"])
def create_user():
    try:
        data = request.json

        newUser = Users(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            store_id=data["store_id"],
            region=data["region"],
            role=data["role"],
            collection=database.get_collection("Users")
        )

        newUser.insert_user()
        print("No error")
        return jsonify({"message": "User inserted successfully!"}), 200

    except Exception as e:
        print(str(e))
        print("Errror")
        return jsonify({"message": "Error inserting User!"}), 500
    
@app.route('/getUsers',methods = ["GET"])
def get_users():
    try:
        people = []

        response = database.get_collection("Users").find({})
        for user in response:
            user["_id"] = str(user["_id"])
            people.append(user)

        logging.info("Successfully retrieved store data")
        return jsonify({"users": people})
    except Exception as e:
        logging.exception(str(e))
        return jsonify({"error": "Error getting user data from database"})
    