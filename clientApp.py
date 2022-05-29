from ObjectDetector import Detector
from flask import Flask, render_template, request, Response, jsonify
import os
from flask_cors import CORS, cross_origin
from common_utils.utils import decodeImage

app = Flask(__name__)

detector = Detector(filename='file.jpg')

RENDER_FACTOR = 35

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "file.jpg"

        self.ObjectDetection = Detector(self.filename)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods = ['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.ObjectDetection.inference('file.jpg')
    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    return jsonify(result)

if __name__ == "__main__":
    clApp = ClientApp()
    port = 5000
    app.run(host='127.0.0.1', port=port)



