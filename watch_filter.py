from web3 import Web3
import asyncio

infura_ws_url = 'wss://ropsten.infura.io/ws/v3/YOUR_KEY'
account = '0x66D0A322E94A8B3be18CCe1E88c34a0E91C28d97'
web3 = Web3(Web3.WebsocketProvider(infura_ws_url))

def handle_event(event):
	print(event)

async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)

def main():
	tx_filter = web3.eth.filter('pending')

	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(
			asyncio.gather(
				log_loop(tx_filter, 2)))
	finally:
		loop.close()

main()