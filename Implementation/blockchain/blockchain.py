from flask import Flask


class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []


# Instantiate the blockchain
blockchain = Blockchain()

# Instantiate the nodes
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
