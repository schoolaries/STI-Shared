# STI-Shared

This is a STI Project based on the Mikrotik RouterOS, aimed at making a RESTFUL API for it which includes CRUD for several functions.
The project utilizes components / applications such as JSON , the Mikrotik API as well as Flask.

Sample Commands for using flask to curl command requests:

IP ADDRESSING:

curl -i -H "Content-Type: application/json" -X POST -d '{"<address>/<subnet>"}' http://localhost:5000/todo/api/mikrotik/createip/<interface>

curl -i http://localhost:5000/todo/api/mikrotik/printip

curl -i -H "Content-Type: application/json" -X PUT -d '{"address":"<address>", "interface":"<interface>"}' http://localhost:5000/todo/api/mikrotik/updateip/<number>

curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/api/mikrotik/deleteip/<number>

VLAN:

curl -i -H "Content-Type: application/json" -X POST -d '{"vlanname":"<vlanname>", "vlanid":"<vlanid>", "vlanbridgename":"<vlanbridgename>", "vlantrafficinterface":"<vlantrafficinterface>"}POST http://localhost:5000/todo/api/mikrotik/createvlan/<interface>

curl -i http://localhost:5000/todo/api/mikrotik/readvlan

curl -i -H "Content-Type: application/json" -X PUT -d '{"vlannumber":"<vlannumber>", "vlanname":"<vlanname>", "vlanid":"<vlanid>"}' http://localhost:5000/todo/api/mikrotik/updatevlan/<interface>

curl -i -H "Content-Type: application/json" -X DELETE -d '{"vlannumber":"<vlannumber>", "vlanbridgenumber":"<vlanbridgenumber>"}' http://localhost:5000/todo/api/mikrotik/deletevlan

FIREWALL:

curl -i -H "Content-Type: application/json" -X POST -d '{"chain":"input", "action":"accept", "rejectw":"icmp-network-unreachable", "protocol":"icmp", "src":"10.10.10.0/24", "dst":"10.10.10.0/24", "log":"no"}' http://localhost:5000/todo/api/mikrotik/firewallrule/create 

curl -i http://localhost:5000/todo/api/mikrotik/firewallrule/print

curl -i -H "Content-Type: application/json" -X PUT -d '{"chain":"input", "action":"drop", "rejectw":"icmp-network-unreachable", "protocol":"icmp", "src":"10.10.10.0/24", "dst":"10.10.10.0/24", "log":"no"}' http://localhost:5000/todo/api/mikrotik/firewallrule/update/1

curl -i http://localhost:5000/todo/api/mikrotik/firewallrule/delete/<numbers>

USER:

curl -i -H "Content-Type: application/json" -X POST -d '{"name":"<name>", "group":"<group>", "password", "<password>"}' http://localhost:5000/todo/api/mikrotik/createuser

curl -i -H "http://localhost:5000/todo/api/mikrotik/printuser

curl -i -H "Content-Type: application/json" -X PUT -d '{"nuser":"<nuser>", "group":"<group>", "password", "<password>"}' http://localhost:5000/todo/api/mikrotik/updateuser/<number>

curl -i -X DELETE http://localhost:5000/todo/api/mikrotik/deleteuser/<numbers>
