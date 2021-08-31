from flask import Flask, send_from_directory, after_this_request,request,make_response
from flask_restful import Resource, Api, reqparse
import dbwork2





app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('host')
parser.add_argument('name')
parser.add_argument('date')
parser.add_argument('size')
parser.add_argument('server')

app = Flask(__name__)


@app.route('/post/', methods = ['GET', 'POST'])
def post():
    args = parser.parse_args()
    out = args['host'],args['name'],args['date'],args['size'],args['server']

    xt = dbwork2.Database()
    xt.insert_data(out)

    return 'kkj'

@app.route('/posterr/', methods = ['GET', 'POST'])
def post():
    args = parser.parse_args()
    out = args['server'],args['content']

    xt = dbwork2.Database()
    xt.insert_err(out)

    return 'kkj'


# class HelloWorld(Resource):
#     post
#
#
#     def get(self):
#         print(self.__dict__)
#         return {'hello': 'get'}
#
#     def put(self):
#         return {'hello': 'put'}
#
#     def delete(self):
#         return {'hello': 'delete'}
#
# api.add_resource(HelloWorld, '/')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='4999')