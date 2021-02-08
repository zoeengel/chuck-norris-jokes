from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    img = requests.get(api_url)
    img_tag = "<img src=" + response['icon_url'] + ">"

    return img_tag + "<strong>Random joke from chuck norris: </strong>" + response['value']


if app == '__main__':
    app.run(debug=True)
