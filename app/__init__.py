from flask import Flask
import pickle

app = Flask(__name__)
server = app.server
model = pickle.load(open('model.pkl', 'rb'))

from app import views
