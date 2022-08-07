# REST was designed to be stateless and for applications to interact with things called resources.

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Api works with resources and every resource has to be a class
class Student(Resource):
    def get(self, name):
        return {'student': name}

api.add_resource(Student, '/student/<string:name>')     # http://127.0.0.1:5000/student/Rolf

app.run(port=5000)