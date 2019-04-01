from urllib.parse import urlsplit

from flask import Flask, jsonify, request

app = Flask(__name__)

plan1 = "[Lahore] [500] [6] ['Badshahi Mosque', 'Lahore Fort', 'Emporium Mall', 'Lahore Museum', 'Badshahi Mosque']"
plan2 = "[Lahore] [700] [6] ['Badshahi Mosque', 'Lahore Fort', 'Emporium Mall', 'Lahore Museum', 'Badshahi Mosque']"
plan3 = "[Lahore] [900] [6] ['Badshahi Mosque', 'Lahore Fort', 'Emporium Mall', 'Lahore Museum', 'Badshahi Mosque']"


@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works'})


@app.route('/budget', methods=['GET'])
def returnbudget():
    return jsonify({'Budgets': plan1})


@app.route('/budgeturl/<string:url>/', methods=['GET'])
def returnplan(url):
    url = str(extract_url_path_and_query())
    arguments=url.split('%2B')
    return jsonify({'Budget': arguments[2]})


def extract_url_path_and_query(full_url=None, no_query=False):
    """
    Convert http://foo.bar.com/aaa/p.html?x=y to /aaa/p.html?x=y

    :param no_query:
    :type full_url: str
    :param full_url: full url
    :return: str
    """
    if full_url is None:
        full_url = request.url
    split = urlsplit(full_url)
    result = split.path or "/"
    if not no_query and split.query:
        result += '?' + split.query
    return result

if __name__ == '__main__':
    app.run(debug=True, port=8080)
