import time
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    time.sleep( 60 )
    return "OpenShift Hello World!"

if __name__ == "__main__":
    application.run()
