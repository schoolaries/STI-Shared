#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
import os, crud, csv, json, subprocess, re

mikrotik = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username =='admin':
		return 'python'
	return None


@auth.error_handler
def unauthorized():
	return make_response(jsonify({'Error':'Unauthorized Access'}), 401)


#CRUD FOR IP ADDRESSING


@mikrotik.route('/todo/api/mikrotik/createip/<interface>', methods=['POST'])
@auth.login_required
def createip(interface):
    ip = request.json['ip']
    subprocess.call(['./test.sh', 'createip', ip, interface])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'ip address': ip, 'interface': interface})


@mikrotik.route('/todo/api/mikrotik/printip', methods=['GET'])
@auth.login_required
def getip():
    subprocess.call(['./test.sh', 'printip'])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'ip': output2})


@mikrotik.route('/todo/api/mikrotik/updateip/<numbers>', methods=['PUT'])
@auth.login_required
def updateip(numbers):
    address = request.json['address']
    interface = request.json['interface']
    subprocess.call(['./test.sh', 'updateip', numbers, address, interface])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'ip': output2})


@mikrotik.route('/todo/api/mikrotik/deleteip/<numbers>', methods=['DELETE'])
@auth.login_required
def deleteip(numbers):
    subprocess.call(['./test.sh', 'deleteip', numbers])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'ip': output2, 'delete': True})


#CRUD FOR WHOLE VLAN 


@mikrotik.route('/todo/api/mikrotik/createvlanall/<vlaninterface>', methods=['POST'])
@auth.login_required
def createvlanall(vlaninterface):
    vlanname = request.json['vlanname']
    vlanid = request.json['vlanid']
    vlanbridgename = request.json['vlanbridgename']
    vlantrafficinterface = request.json['vlantrafficinterface']
    subprocess.call(['./test.sh', 'createvlanall', vlaninterface, vlanname, vlanid, vlanbridgename, vlantrafficinterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/readvlanall', methods=['GET'])
@auth.login_required
def readvlanall():
    subprocess.call(['./test.sh', 'readvlanall'])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/updatevlanall/<vlaninterface>', methods=['PUT'])
@auth.login_required
def updatevlanall(vlaninterface):
    vlannumber = request.json['vlannumber']
    vlanname = request.json['vlanname']
    vlanid = request.json['vlanid']
    subprocess.call(['./test.sh', 'updatevlanall', vlannumber, vlanname, vlanid, vlaninterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/deletevlanall', methods=['DELETE'])
@auth.login_required
def deletevlanall():
    vlannumber = request.json['vlannumber']
    vlanbridgenumber = request.json['vlanbridgenumber']
    subprocess.call(['./test.sh', 'deletevlanall', vlannumber, vlanbridgenumber])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


#CRUD FOR VLAN ONLY

@mikrotik.route('/todo/api/mikrotik/createvlan/<vlaninterface>', methods=['POST'])
@auth.login_required
def createvlan(vlaninterface):
    vlanname = request.json['vlanname']
    vlanid = request.json['vlanid']
    subprocess.call(['./test.sh', 'createvlan', vlaninterface, vlanname, vlanid])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/readvlan', methods=['GET'])
@auth.login_required
def readvlan():
    subprocess.call(['./test.sh', 'readvlan'])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/updatevlan/<vlaninterface>', methods=['PUT'])
@auth.login_required
def updatevlan(vlaninterface):
    vlannumber = request.json['vlannumber']
    vlanname = request.json['vlanname']
    vlanid = request.json['vlanid']
    subprocess.call(['./test.sh', 'updatevlan', vlannumber, vlanname, vlanid, vlaninterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/deletevlan/<numbers>', methods=['DELETE'])
@auth.login_required
def deletevlan(numbers):
    subprocess.call(['./test.sh', 'deletevlan', numbers])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2, 'delete': True})


#CRUD FOR BRIDGES


@mikrotik.route('/todo/api/mikrotik/createbridge', methods=['POST'])
@auth.login_required
def createbridge():
    bridgename = request.json['bridgename']
    subprocess.call(['./test.sh', 'createbridge', bridgename])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridge': output2})


@mikrotik.route('/todo/api/mikrotik/readbridge', methods=['GET'])
@auth.login_required
def readbridge():
    subprocess.call(['./test.sh', 'readbridge'])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridge': output2})


@mikrotik.route('/todo/api/mikrotik/updatebridge/<bridgenumber>', methods=['PUT'])
@auth.login_required
def updatebridge(bridgenumber):
    bridgename = request.json['bridgename']
    subprocess.call(['./test.sh', 'updatebridge', bridgenumber, bridgename])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridge': output2})


@mikrotik.route('/todo/api/mikrotik/deletebridge/<bridgenumbers>', methods=['DELETE'])
@auth.login_required
def deletebridge(bridgenumbers):
    subprocess.call(['./test.sh', 'deletebridge', bridgenumbers])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridge': output2, 'delete': True})


#CRUD FOR BRIDGE PORTS


@mikrotik.route('/todo/api/mikrotik/createbridgeport', methods=['POST'])
@auth.login_required
def createbridgeport():
    bridgeportname = request.json['bridgeportname']
    bridgeinterface = request.json['bridgeinterface']
    bridgeportinterface = request.json['bridgeportinterface']
    subprocess.call(['./test.sh', 'createbridgeport', bridgeportname, bridgeinterface, bridgeportinterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridgeport': output2})


@mikrotik.route('/todo/api/mikrotik/readbridgeport', methods=['GET'])
@auth.login_required
def readbridgeport():
    subprocess.call(['./test.sh', 'readbridgeport'])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridgeport': output2})


@mikrotik.route('/todo/api/mikrotik/updatebridgeport/<bridgeportnumber>', methods=['PUT'])
@auth.login_required
def updatebridgeport(bridgeportnumber):
    bridgeportname = request.json['bridgeportname']
    bridgeportinterface = request.json['bridgeportinterface']
    subprocess.call(['./test.sh', 'updatebridgeport', bridgeportnumber, bridgeportname, bridgeportinterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridgeport': output2})


@mikrotik.route('/todo/api/mikrotik/deletebridgeport/<bridgeportnumber>', methods=['DELETE'])
@auth.login_required
def deletebridgeport(bridgeportnumber):
    subprocess.call(['./test.sh', 'deletebridgeport', bridgeportnumber])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridgeport': output2, 'delete': True})


#CRUD FOR FIREWALL RULES


@mikrotik.route('/todo/api/mikrotik/firewallrule/create', methods=['POST'])
@auth.login_required
def create_rule():
	chain = request.json['chain']
	action = request.json['action']
	rejectw = request.json['rejectw']
	protocol = request.json['protocol']
	src = request.json['src']
	dst = request.json['dst']
	log = request.json['log']

	subprocess.call(['./test.sh', 'createrule', chain, action, rejectw, protocol, src, dst, log])

	with open('file.txt') as f:
		output = f.read()

	return jsonify({'chain': chain, 'action': action, 'reject-with': rejectw, 'protocol': protocol, 'source address': src, 'destination address': dst, 'log': log})


@mikrotik.route('/todo/api/mikrotik/firewallrule/print', methods=['GET'])
@auth.login_required
def get_rule():
	subprocess.call(['./test.sh', 'printrule'])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'rules': output2})


@mikrotik.route('/todo/api/mikrotik/firewallrule/update/<numbers>', methods=['PUT'])
@auth.login_required
def update_rule(numbers):
    	chain = request.json['chain']
	action = request.json['action']
	rejectw = request.json['rejectw']
	protocol = request.json['protocol']
	src = request.json['src']
	dst = request.json['dst']
	log = request.json['log']

    	subprocess.call(['./test.sh', 'updaterule', numbers, chain, action, rejectw, protocol, src, dst, log])

    	with open('file.txt') as f:
		output = f.read()
                output2 = re.split('\n', output)
    	return jsonify({'rule': output2})


@mikrotik.route('/todo/api/mikrotik/firewallrule/delete/<numbers>', methods=['DELETE'])
@auth.login_required
def delete_rule(numbers):
	subprocess.call(['./test.sh', 'deleterule', numbers])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'rules': output2, 'delete': True})


#CRUD FOR USERS


@mikrotik.route('/todo/api/mikrotik/createuser', methods=['POST'])
@auth.login_required
def createuser():
    name = request.json['name']
    group = request.json['group']
    password = request.json['password']

    subprocess.call(['./test.sh', 'createuser', name, group, password])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'name':name, 'group':group, 'password':password})


@mikrotik.route('/todo/api/mikrotik/printuser', methods=['GET'])
@auth.login_required
def getuser():
    subprocess.call(['./test.sh', 'printuser'])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'user': output2})

@mikrotik.route('/todo/api/mikrotik/updateuser/<numbers>', methods=['PUT'])
@auth.login_required
def updateuser(numbers):
    nuser = request.json['nuser']
    group = request.json['group']
    password = request.json['password']

    subprocess.call(['./test.sh', 'updateuser', numbers, nuser, group, password])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'user': output2})

@mikrotik.route('/todo/api/mikrotik/deleteuser/<numbers>', methods=['DELETE'])
@auth.login_required
def deleteuser(numbers):
    subprocess.call(['./test.sh', 'deleteuser', numbers])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'user': output2, 'delete': True})


#CRUD FOR IP ROUTE


@mikrotik.route('/todo/api/mikrotik/route/print', methods=['GET'])
@auth.login_required
def printRoute():
	subprocess.call(['./test.sh', 'printroute'])
	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Route': output2})

@mikrotik.route('/todo/api/mikrotik/route/create', methods=['POST'])
@auth.login_required
def createRoute():
	dst = request.json['dst']
	src = request.json['src']
	gateway = request.json['gateway']
	subprocess.call(['./test.sh', 'createroute', dst, src, gateway])
	with open('file.txt') as f:
		output = f.read()
	return jsonify({'dst-address': dst, 'pref-src':src, 'gateway': gateway})

@mikrotik.route('/todo/api/mikrotik/route/update=<numbers>', methods=['PUT'])
@auth.login_required
def updateRoute(numbers):
	dst = request.json['dst']
	src = request.json['src']
	gateway = request.json['gateway']
	subprocess.call(['./test.sh', 'updateroute', numbers, dst, src, gateway])
	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Updated Route': output2})

@mikrotik.route('/todo/api/mikrotik/route/delete=<numbers>', methods=['DELETE'])
@auth.login_required
def deleteRoute(numbers):
	subprocess.call(['./test.sh', 'deleteroute', numbers])
	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Route': output2, 'delete':True})

if __name__ == '__main__':
    mikrotik.run(debug=True)
