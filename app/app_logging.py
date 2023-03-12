import logging
from flask import Flask

app = Flask(__name__)

logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
handler = logging.FileHandler('/var/log/flask.log') # creates handler for the log file
logger.addHandler(handler) # adds handler to the werkzeug WSGI logger

