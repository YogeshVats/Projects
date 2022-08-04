from flask import Flask    # flask is a repo and Flask is a class


app = Flask(__name__)      # creating flask app and giving it a specific name using __name__

@app.route('/')     # 'http://www.google.com/'  Home route
def home():                 # name of this method doesn't matter and can be anything
    print("Hello World!")
    return "Hello World!"


app.run(port = 5000)        # running flask application and giving it port 5000