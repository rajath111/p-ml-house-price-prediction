from flask import Flask, Response
from flask_restful import Api, Resource

from input_parser import PredictRequestParser
from model_loader import ModelLoader

app = Flask(__name__)
api = Api(app)
parser = PredictRequestParser()
model = ModelLoader.load()


class Predict(Resource):
    def post(slef):
        if model is None:
            return Response({'message': 'Model loading failed'}, status=500)
            
        try:
            args = parser.parse_args()
        except Exception as e:
            print(e)
            return Response("Incorrect Input", status=400)

        predicted_value = model.predict([[args.get('rm'), args.get('lstst'), args.get('ptratio')]])
        return {'PredictedPrice': predicted_value[0]}


api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')