from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/add_marker', methods=['POST'])
def add_marker():
    print("Received add marker request")
    print(request.json)
    return Response(status=201)


@app.route('/get_markers', methods=['GET'])
def get_markers():
    return {
        "markers": [
            {
                "posX": 100,
                "posY": 100,
            },
            {
                "posX": 200,
                "posY": 200,
            },
            {
                "posX": 300,
                "posY": 300,
            }
        ]
    }



if __name__ == '__main__':
    app.run()
