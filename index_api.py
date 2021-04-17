
import json
import requests
from flask import (
    Flask,
    make_response,
    jsonify,
    request,
    send_file,
    send_from_directory,
    abort,
)
from flask_cors import CORS
from PIL import Image
from orai_prediction import main_flower

app = Flask(__name__)
CORS(app)


def response_body(status, data):
    status = int(status)
    if status == 0:
        status = "error"
    if status == 1:
        status = "success"

    response_body_json = {
        "status": status,
        "data": data
    }
    res = make_response(jsonify(response_body_json), 200)
    return res


def file_storage_to_memfile(file):
    image = Image.open(file)
    image = image.convert("RGB")
    return image


@app.route("/", methods=['GET'])
def get_service():
    return 'flower_classification'


@app.route("/", methods=['POST'])
def human_portrait():
    # get data from user
    try:
        input_source = file_storage_to_memfile(request.files['input_source'])

    except Exception as error:
        error = str(error)
        print(error)
        return response_body(status=0, data=error)

    try:
        result = main_flower(input_source)
        return response_body(status=1, data=result)
    except Exception as error:
        error = str(error)
        print(error)
        return response_body(status=0, data=error)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
