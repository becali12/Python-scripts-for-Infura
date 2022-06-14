# Python-scripts-for-Infura

This repository contains scripts I've created for the Support Tips category on the Infura community. 



**watch.py** - continuosly searches the latest block for ETH transactions incoming to a specified address.

**watch_subscribe.py** - uses websockets to subscribe to the pending transactions pool, then looks for ETH transactions incoming to a specified address.

**watch_filter.py** - attempt to do the same as above using filters, not working due to an Infura limitation

**send_tx_1559** - can be used to send an eip-1559 transaction
