#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import api

mikrotik = Flask(__name__)

@mikrotik.route('/todo/api/mikrotik/ip', methods=['GET'])
def getip():
    return jsonify({'ip': api.printIp()})

if __name__ == '__main__':
    mikrotik.run(debug=True)
