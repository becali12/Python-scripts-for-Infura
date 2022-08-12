from web3 import Web3
import asyncio
import json
from websockets import connect

infura_http_url = 'https://mainnet.infura.io/v3/YOUR_KEY'
infura_ws_url = 'wss://mainnet.infura.io/ws/v3/YOUR_KEY'

web3 = Web3(Web3.HTTPProvider(infura_http_url))

options721 = {
	'topics': [
		web3.sha3(text='Transfer(address,address,uint256)').hex()
	]
}

options1155 = {
	'topics': [
		web3.sha3(text='TransferSingle(address,address,address,uint256,uint256)').hex()
	]
}

request_721 = {"jsonrpc":"2.0", "id": 1, "method": "eth_subscribe", "params": ["logs", options721]}
request_1155 = {"jsonrpc":"2.0", "id": 1, "method": "eth_subscribe", "params": ["logs", options1155]}
request_string_721 = json.dumps(request_721)
request_string_1155 = json.dumps(request_1155)

async def get_event_1155():
	async with connect(infura_ws_url) as ws:
		await ws.send(request_string_1155)
		subscription_response = await ws.recv()
		print(subscription_response)
		while True:
			try:
				message = await asyncio.wait_for(ws.recv(), timeout=60)
				event = json.loads(message)
				result = event['params']['result']
				# there are 24 zeros before the actual address in the log's topics
				# 26 = 24 + 2 more characters for the '0x' characters
				from_address = '0x' + result['topics'][2][26:]
				to_address = '0x' + result['topics'][3][26:]
				# data is spread in two 64 bytes sections - first is token ID, second is value
				# to get the token ID we convert the first 66 characters of data to int
				# 66 = 64 + 2 more chars for '0x' at the beginning of the data string
				token_id = int(result['data'][:66], 16)
				token_address = result['address']
				block = int(result['blockNumber'], 16)
				tx_hash = result['transactionHash']
				print(
					"New ERC-1155 transaction with hash {} found in block {} From: {} To: {} Token Address: {} Token ID: {}".format(
						tx_hash, block, from_address, to_address, token_address, token_id))
				pass
			except:
				pass

async def get_event_721():
	async with connect(infura_ws_url) as ws:
		await ws.send(request_string_721)
		subscription_response = await ws.recv()
		print(subscription_response)
		while True:
			try:
				message = await asyncio.wait_for(ws.recv(), timeout=60)
				event = json.loads(message)
				print(event)
				if len(event['params']['result']['topics']) == 4:
					result = event['params']['result']
					from_address = '0x' + result['topics'][1][26:]
					to_address = '0x' + result['topics'][2][26:]
					token_id = int(result['topics'][3], 16)
					token_address = result['address']
					block = int(result['blockNumber'], 16)
					tx_hash = result['transactionHash']
					print("New ERC-721 transaction with hash {} found in block {} From: {} To: {} Token Address: {} Token ID: {}".format(tx_hash, block, from_address, to_address, token_address, token_id))
				pass
			except:
				pass


if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	while True:
		# loop.run_until_complete(get_event_1155())
		loop.run_until_complete(get_event_721())

