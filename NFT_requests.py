import requests
import json

infura_url = 'https://nft.api.infura.io/networks/1/'
proj_id = 'YOUR_PROJECT_ID'
proj_secret = 'YOUR_PROJECT_SECRET'

# gets the NFT collection's metadata
# token_address is a String by default
def getCollectionMetadata(token_address):
	request_url = infura_url + 'nfts/' + token_address
	response = requests.get(request_url, auth=(proj_id, proj_secret))
	if response.status_code == 200:
		res = response.json()
		print(res)


# gets a specific NFT's metadata - based on the token ID
# token_address, token_id are strings
def getNFTMetadata(token_address, token_id):
	request_url = infura_url + 'nfts/' + token_address + '/tokens/' + token_id
	response = requests.get(request_url, auth=(proj_id, proj_secret))
	if response.status_code == 200:
		res = response.json()
		print(res)


def getNFTsByCollection(token_address):
	request_url = infura_url + 'nfts/' + token_address + '/tokens/'
	response = requests.get(request_url, auth=(proj_id, proj_secret))
	if response.status_code == 200:
		res = response.json()
		print(res)


# address is a string
def getNFTsOwned(address):
	request_url = infura_url + 'accounts/' + address + '/assets/nfts/'
	response = requests.get(request_url, auth=(proj_id, proj_secret))
	if response.status_code == 200:
		res = response.json()
		if res['total'] == 0:
			print('No NFTs owned by ' + address)
		else:
			print(res)


if __name__ == "__main__":
	getNFTsOwned('0x0a267cf51ef038fc00e71801f5a524aec06e4f07')
	# getCollectionMetadata('0x31d45de84fdE2fB36575085e05754a4932DD5170')
	# getNFTMetadata('0x31d45de84fdE2fB36575085e05754a4932DD5170', '5')
	# getNFTsByCollection('0x31d45de84fdE2fB36575085e05754a4932DD5170')
