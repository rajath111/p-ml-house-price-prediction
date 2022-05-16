from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import pickle

predict_input_args = reqparse.RequestParser()
predict_input_args.add_argument('rm', type=float)
predict_input_args.add_argument('lstst', type=float)
predict_input_args.add_argument('ptratio', type=float)


app = Flask(__name__)
api = Api(app)

model = None
with open('model/modelfile', 'rb') as f:
    model = pickle.load(f)

class Predict(Resource):
    def post(slef):
        # print('Request json {}'.format(request.json))
        args = predict_input_args.parse_args()
        predicted_value = model.predict([[args['rm'], args['lstst'], args['ptratio']]])
        return {'PredictedPrice': predicted_value[0]}

class Hello(Resource):
    def get(self):
        return 'Hello there...'
        


api.add_resource(Predict, '/predict')
api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')