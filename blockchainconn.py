import random
import sys
import base64

import json

from web3 import Web3
from solc import compile_standard

# Solidity source code
compiled_sol = compile_standard({
     "language": "Solidity",
     "sources": {
         "wsm.sol": {
             "content": '''

pragma solidity >=0.4.22 <0.7.0;
contract Waste_Management {
    string public keyname;
    uint public keyCount = 0;
    mapping(uint => Product) public keys;

    struct Product {
        uint id;
        string name;
        address payable owner;
        bool purchased;
    }

    event ProductCreated(
        uint id,
        string name,
        address payable owner,
        bool purchased
    );

    event ProductPurchased(
        uint id,
        string name,
        address payable owner,
        bool purchased
    );

    constructor(string memory n) public {
        keyname = n;
    }

    function createProduct(string memory _name) public {
        // Require a valid name
        require(bytes(_name).length > 0);
        // Require a valid price
        // Increment product count
        keyCount ++;
        // Create the product
        keys[keyCount] = Product(keyCount, _name, msg.sender, false);
        // Trigger an event
        emit ProductCreated(keyCount, _name, msg.sender, false);
    }

  
    
    function getPro(uint id)
        public
        returns (string memory name)
    {
        Product memory p = keys[id];
        
        return (p.name);
    }
}
               '''
         }
     },
     "settings":
         {
             "outputSelection": {
                 "*": {
                     "*": [
                         "metadata", "evm.bytecode"
                         , "evm.bytecode.sourceMap"
                     ]
                 }
             }
         }
 })



	# Submit the transaction that deploys the contract
def deploying(name):
    w3 = Web3(Web3.EthereumTesterProvider())

	# set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]

            # get bytecode
    bytecode = compiled_sol['contracts']['wsm.sol']['Waste_Management']['evm']['bytecode']['object']

            # get abi
    abi = json.loads(compiled_sol['contracts']['wsm.sol']['Waste_Management']	['metadata'])['output']['abi']

    pb = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash,tx_receipt,p1="","",""
    tx_hash = pb.constructor(name).transact()

    tx_hash = pb.constructor(name).transact()

	# Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print("tx_receipt.contractAddress: ",tx_receipt.contractAddress)
    p1 = w3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=abi
            )


def createKey(name):
    w3 = Web3(Web3.EthereumTesterProvider())

	# set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]

            # get bytecode
    bytecode = compiled_sol['contracts']['wsm.sol']['Waste_Management']['evm']['bytecode']['object']

            # get abi
    abi = json.loads(compiled_sol['contracts']['wsm.sol']['Waste_Management']	['metadata'])['output']['abi']

    pb = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash,tx_receipt,p1="","",""
    tx_hash = pb.constructor(name).transact()

	# Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print("tx_receipt.contractAddress: ",tx_receipt.contractAddress)
    p1 = w3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=abi
            )
    tx_hash = p1.functions.createProduct(name).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print(tx_hash)
    print(tx_receipt)



def getKey(pid):
    w3 = Web3(Web3.EthereumTesterProvider())

            # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]

            # get bytecode
    bytecode = compiled_sol['contracts']['wsm.sol']['Waste_Management']['evm']['bytecode']['object']

            # get abi
    abi = json.loads(compiled_sol['contracts']['wsm.sol']['Waste_Management']	['metadata'])['output']['abi']

    pb = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash,tx_receipt,p1="","",""
    tx_hash = pb.constructor("name").transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print("tx_receipt.contractAddress: ",tx_receipt.contractAddress)
    p1 = w3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=abi
            )

    tx_hash = p1.functions.getPro(int(pid)).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print(tx_hash)
    print(tx_receipt)
deploying("name")
createKey("pro")
getKey(0)
