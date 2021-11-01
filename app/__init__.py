from flask import Flask
import pickle

app = Flask(__name__)



from app import views,main
