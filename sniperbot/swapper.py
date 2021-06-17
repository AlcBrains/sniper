from web3 import Web3

import config as cfg


class Swapper(BaseException):

    def __init__(self, to_address, abi):
        self.contractAddress = to_address
        self.abi = abi
        self.web3 = Web3(Web3.HTTPProvider(cfg.quicknode_api_key))

    #
    def check_connect(self):
        # Sanity check.
        raise ConnectionError('Couldn\'t connect to quicknode!') if self.web3.isConnected() != 1 else print('Connected')

        # contract = self.web3.eth.contract(address=self.contractAddress, abi=self.abi)
        # print(contract.functions.totalSupply().call())

    def swap(self, contract_address, amount, gas_price):
        # get the nonce. Prevents from sending the transaction twice
        nonce = self.web3.eth.getTransactionCount(cfg.from_address)

        # build a transaction in a dictionary
        tx = {
            'nonce': nonce,
            'to': contract_address,
            'value': self.web3.toWei(amount, 'bsc'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei(gas_price, 'gwei')
        }

        # sign the transaction
        signed_tx = self.web3.eth.account.sign_transaction(tx, cfg.private_api_key)

        # send transaction
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # get transaction hash
        print(self.web3.eth.get_transaction_receipt(tx_hash))
