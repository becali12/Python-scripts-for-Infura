# Python scripts for Infura

This repository contains scripts I've created for the Support Tips category on the Infura community and for the Infura Docs. 



**watch.py** - continuosly searches the latest block for ETH transactions incoming to a specified address. It's online here: https://community.infura.io/t/web3-py-how-to-monitor-ethereum-transfers-to-an-address-in-python/5448

**watch_subscribe.py** - uses websockets to subscribe to the pending transactions pool, then looks for ETH transactions incoming to a specified address. It's online here: https://community.infura.io/t/web3-py-how-to-subscribe-to-pending-ethereum-transactions-in-python/5409

**watch_filter.py** - attempt to do the same as above using filters, not working due to an Infura limitation

**send_tx_1559.py** - can be used to send an eip-1559 transaction. It's online here: https://docs.infura.io/infura/tutorials/ethereum/send-a-transaction/send-a-transaction-1

**monitorNFT.py** - monitors ERC-721 and ERC-1155 transfers using websockets. It's online here: https://community.infura.io/t/web3-py-how-to-track-nft-erc-721-1155-transfers-and-mints/5624

**NFT_requests.py** - can be used to perform simple read operations regarding NFTs, like fetching Metadata or the NFTs owned by an address.It's online here: https://community.infura.io/t/python-how-to-use-the-infura-nft-api/5789
