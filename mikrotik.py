#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import os, crud, csv

mikrotik = Flask(__name__)

@mikrotik.route('/todo/api/mikrotik/ip', methods=['GET'])
def getip():
    os.system('./test.sh')
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'ip': output})

@mikrotk.route('/todo/api/mikrotik/ip', 

if __name__ == '__main__':
    mikrotik.run(debug=True)
