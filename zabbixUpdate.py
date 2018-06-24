from zabbix_api import ZabbixAPI
import csv, sys

request = ZabbixAPI(server = "http://192.168.56.102/zabbix")
request.login("Admin","zabbix")

def update():
    file = csv.reader(open('python_rest/zabbix.csv'), delimiter=';')
    for [hostid,location] in file:
        request.host.update({"hostid": hostid, "inventory": {"location": location}})

def export():
    data = request.host.get({"groupids": "4", "output": ["host"], "selectInterfaces": ["ip"], "selectInventory": ["location"]})
    for host in data:
        print (host)

if __name__ == '__main__':
#    update()
    export()
