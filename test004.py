from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to change for this resource')
args = parser.parse_args()


class TodoSImple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}
        # return {'hello': 'world'}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


class Todo1(Resource):
    def get(self):
        return {'task': 'Hello world'}


class Todo2(Resource):
    def get(self):
        return {'task': 'Hello world'}, 201


class Todo3(Resource):
    def get(self):
        return {'task': 'Hello world'}, 201, {'Etag', 'some-opaque-string'}


api.add_resource(TodoSImple, '/<string:todo_id>')
api.add_resource(Todo1, '/', '/todo1')
api.add_resource(Todo2, '/', '/todo2')

if __name__ == '__main__':
    app.run(debug=True)
