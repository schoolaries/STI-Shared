#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import os, crud, csv, json, subprocess

mikrotik = Flask(__name__)

@mikrotik.route('/todo/api/mikrotik/createip/<interface>', methods=['POST'])
def createip(interface):
    ip = request.json['ip']
    subprocess.call(['./test.sh', 'create', ip, interface])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'ip address': ip, 'interface': interface})


@mikrotik.route('/todo/api/mikrotik/printip', methods=['GET'])
def getip():
    subprocess.call(['./test.sh', 'print'])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'ip': output})

@mikrotik.route('/todo/api/mikrotik/updateip/<numbers>', methods=['PUT'])
def updateip(numbers):
    address = request.json['address']
    interface = request.json['interface']
    subprocess.call(['./test.sh', 'update', numbers, address, interface])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'ip': output})

@mikrotik.route('/todo/api/mikrotik/deleteip/<numbers>', methods=['DELETE'])
def deleteip(numbers):
    subprocess.call(['./test.sh', 'delete', numbers])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'ip': output, 'delete': True})

if __name__ == '__main__':
    mikrotik.run(debug=True)
