import requests

proj_id = '229f0...'
proj_secret = 'c29cd...'
infura_url = 'https://mainnet.infura.io/v3/229f05...'

requests_json = [
	{"jsonrpc": "2.0", "id": 1, "method": "eth_blockNumber", "params": []},
	{"jsonrpc": "2.0", "id": 2, "method": "eth_blockNumber", "params": []},
	{"jsonrpc": "2.0", "id": 3, "method": "eth_blockNumber", "params": []}
]

def batch():
    response = requests.post(url=infura_url, json=requests_json, auth=(proj_id, proj_secret))
    if response.status_code == 200:
        res = response.json()
        for i in res:
            print(i['result'])


if __name__ == "__main__":
    batch()
