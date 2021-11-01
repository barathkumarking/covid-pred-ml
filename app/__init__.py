from flask import Flask
import pickle
server = app.server
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

from app import views
