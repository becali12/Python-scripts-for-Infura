import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

infura_url = ('https://%s.infura.io/v3/%s' %(os.getenv('ETHEREUM_NETWORK'), os.getenv('INFURA_PROJECT_ID')))
private_key = os.getenv('SIGNER_PRIVATE_KEY')
from_account = '0x66D0A322E94A8B3be18CCe1E88c34a0E91C28d97'
to_account = '0x895c21B0417328CfB3eA5c8F48b0497B2110BA06'
web3 = Web3(Web3.HTTPProvider(infura_url))
nonce = web3.eth.getTransactionCount(from_account)

tx = {
    'type': '0x2',
    'nonce': nonce,
    'from': from_account,
    'to': to_account,
    'value': web3.toWei(0.01, 'ether'),
    'maxFeePerGas': web3.toWei('250', 'gwei'),
    'maxPriorityFeePerGas': web3.toWei('3', 'gwei'),
    'chainId': 3
}

gas = web3.eth.estimateGas(tx)
tx['gas'] = gas
signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print("Transaction hash: " + str(web3.toHex(tx_hash)))