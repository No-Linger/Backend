from flask import Flask
import firebase_admin
from firebase_admin import credentials
from config import Config


cred = credentials.Certificate(Config.SERVICE_ACCOUNT_KEY)
firebase_admin.initialize_app(cred)

app = Flask(__name__)

from app import routes