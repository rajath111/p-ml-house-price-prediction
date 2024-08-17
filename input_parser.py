from flask_restful import reqparse


class PredictRequestParser:
    def __init__(self):

        self.predict_input_args = reqparse.RequestParser()
        self.predict_input_args.add_argument('rm', type=float)
        self.predict_input_args.add_argument('lstst', type=float)
        self.predict_input_args.add_argument('ptratio', type=float)

    def parse_args(self):
        return self.predict_input_args.parse_args()