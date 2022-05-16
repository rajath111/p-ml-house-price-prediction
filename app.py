from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle

predict_input_args = reqparse.RequestParser()
predict_input_args.add_argument('rm', type=float, location='form')
predict_input_args.add_argument('lstst', type=float, location='form')
predict_input_args.add_argument('ptratio', type=float, location='form')


app = Flask(__name__)
api = Api(app)

model = None
with open('model/modelfile', 'rb') as f:
    model = pickle.load(f)

class Predict(Resource):
    def post(slef):
        args = predict_input_args.parse_args()
        predicted_value = model.predict([[args['rm'], args['lstst'], args['ptratio']]])
        print('Predicted Value {}'.format(predicted_value))
        return {'PredictedPrice': predicted_value[0]}
        


api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(port=4300)