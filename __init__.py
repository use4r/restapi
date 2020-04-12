# __init__.py

from flask import Flask

# определение приложения
app = Flask(__name__)

from app import usersData
