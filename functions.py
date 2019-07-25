import requests
import json


#Units > 0 is a buy. < 0  is a sell
def marketOrder(pair, units):
    Headers = {
    'Content-type': 'application/json', #Miht be unneccecary
    'Authorization': TOKEN
    }#end Headers
    
    data = {
    'order': {
    "units": units,
    "instrument": pair,
    "timeInForce": "FOK",
    "type": "MARKET",
    "positionFill": "DEFAULT"
    }
    }#End data
    
    r = requests.post("https://api-fxpractice.oanda.com/v3/accounts/101-001-10674043-001/orders",data = json.dumps(body), headers = Headers, json={"key": "value"})
    order_Response = json.loads(r.text)
    return order_Response


def marginInUse():
    a = requests.get('https://api-fxpractice.oanda.com/v3/accounts/101-001-10674043-001', headers = Headers)
    print(a.text)
    account_Dict = json.loads(a.text)
    print(account_Dict['account']['marginUsed'])

def accountBalance():
    a = requests.get('https://api-fxpractice.oanda.com/v3/accounts/101-001-10674043-001', headers = Headers)
    print(a.text)
    account_Dict = json.loads(a.text)
    return (account_Dict['account']['balance'])

