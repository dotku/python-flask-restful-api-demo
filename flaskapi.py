from flask import Flask, json, request
from nanoid import generate

shoppingItems = [{"id": generate(), "content": "apple"},
                 {"id": generate(), "content": "banna"},
                 {"id": generate(), "content": "chiken"},
                 {"id": generate(), "content": "duck"}]

api = Flask(__name__)


@api.route("/", methods=['GET'])
def get_shopping_items():
    return json.dumps(shoppingItems)


@api.route("/", methods=['POST'])
def post_shopping_items():
    data = request.get_json()
    shoppingItems.append({"id": generate(), "content": data["content"]})
    return json.dumps(shoppingItems)


if __name__ == '__main__':
    api.run()
