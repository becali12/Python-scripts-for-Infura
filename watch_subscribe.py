from web3 import Web3
import asyncio
import json
import requests
from websockets import connect

infura_ws_url = 'wss://ropsten.infura.io/ws/v3/YOUR_KEY'
infura_http_url = 'https://ropsten.infura.io/v3/YOUR_KEY'
account = '0x66D0A322E94A8B3be18CCe1E88c34a0E91C28d97'
web3 = Web3(Web3.HTTPProvider(infura_http_url))


# can be called to check the number of block confirmations for a transaction
def confirmations(tx_hash):
    tx = web3.eth.get_transaction(tx_hash)
    return web3.eth.block_number - tx.blockNumber

async def get_event():
    async with connect(infura_ws_url) as ws:

        await ws.send('{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}')
        subscription_response = await ws.recv()
        print(subscription_response)
        
        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=10)
                response = json.loads(message)
                txHash = response['params']['result']
                tx = web3.eth.get_transaction(txHash)
                if tx.to == account:
                	print("Pending transaction found with the following details:")
                	print({
                            "hash": txHash,
                            "from": tx["from"],
                            "value": web3.fromWei(tx["value"], 'ether')
                            })
                pass
            except:
                pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(get_event())