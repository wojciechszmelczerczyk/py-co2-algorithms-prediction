from flask import Flask, request
import numpy as np

app = Flask(__name__)


@app.route("/prediction", methods=['POST'])
def co2_prediction():
    
    # sensors data
    data = request.get_json()

    ## ml algorithms logic

    return data


if __name__ == '__main__':
    app.run()