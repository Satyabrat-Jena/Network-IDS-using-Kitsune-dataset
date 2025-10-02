# Make sure necessary libraries are imported
from web3 import Web3
import json
import pandas as pd # Keep pandas import as it's used earlier in the notebook
import numpy as np  # Keep numpy import as it's used earlier in the notebook
# Remove IPython imports as they are not strictly needed for this cell's core logic
# from IPython import get_ipython
# import warnings

# --- IMPORTANT ---
# Make sure your Ganache (or local blockchain node) is RUNNING
# and accessible at http://127.0.0.1:7545 BEFORE running this cell.
# If Ganache is not running, you will get a ConnectionRefusedError.

# Connect to Ganache
ganache_url = 'http://127.0.0.1:7545'
print(f"Attempting to connect to Ganache at: {ganache_url}")
try:
    w3 = Web3(Web3.HTTPProvider(ganache_url))

    # Check the connection
    if not w3.is_connected():
        # If connection fails, raise a specific error explaining the issue
        raise ConnectionError(f"Failed to connect to Ganache at {ganache_url}. "
                              "Please ensure Ganache is running and accessible.")

    print("Connection to Ganache successful.")

except ConnectionError as e:
    # Catch our specific connection error and print a message, then exit gracefully
    print(f"Error: {e}")
    # You might want to exit the cell execution here in a real notebook environment
    # For demonstration, we'll set w3 to None to prevent further errors.
    w3 = None
except Exception as e:
    # Catch any other unexpected errors during connection
    print(f"An unexpected error occurred during connection: {e}")
    w3 = None


# Continue only if the connection was successful
if w3 is not None and w3.is_connected():
    # Contract address and ABI from Remix
    # --- IMPORTANT ---
    # Replace with the actual contract address and ABI from your deployed contract on Ganache
    # Note: The ABI provided here looks like a placeholder from a previous cell.
    # Please ensure you are using the *correct* ABI for your deployed contract from Ganache.
    # The ABI in ipython-input-148-354c77695896 seems more complete and corrects boolean values.
    # Let's use the more complete ABI from ipython-input-148-354c77695896.
    contract_address = "0x8d883f7e0422e0eC626Cd79591e18c41AdDfcE1c"  # From Step 5
    contract_abi = [
        {
            "inputs": [
                {
                    "internalType": "string",
                    "name": "_features",
                    "type": "string"
                }
            ],
            "name": "logPacket",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address"
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "timestamp",
                    "type": "uint256"
                },
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "features",
                    "type": "string"
                }
            ],
            "name": "PacketLogged",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "index",
                    "type": "uint256"
                }
            ],
            "name": "getPacket",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "getPacketCount",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "name": "packets",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "sender",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "timestamp",
                    "type": "uint256"
                },
                {
                    "internalType": "string",
                    "name": "features",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]


    # Create contract instance
    try:
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)
        print("Contract instance created.")
    except Exception as e:
        print(f"Failed to create contract instance: {e}")
        print("Please ensure the contract address and ABI are correct and match the deployed contract.")
        contract = None # Set contract to None to prevent further errors

    # Use an account from Ganache
    # --- IMPORTANT ---
    # Replace with the actual Ganache account address and its private key
    # Be extremely cautious with private keys! Never hardcode them in production code.
    account = "0xd5babe02BEb5e8806EbC7b51654eDc24e348392b"  # From Ganache
    private_key = "0xd888507641b3b2e62c06bb86bb15cf34792b63a673c0f00d53f12cf5589987a2"  # From Ganache

    # Example: Log a feature string
    feature_str = "[1.2, 3.4, 5.6]"

    # Proceed only if the contract instance was successfully created
    if contract is not None:
        try:
            nonce = w3.eth.get_transaction_count(account)
            tx = contract.functions.logPacket(feature_str).build_transaction({
                'from': account,
                'nonce': nonce,
                'gas': 2000000, # May need to adjust gas limit depending on string size
                'gasPrice': w3.to_wei('20', 'gwei')
            })
            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            # Using timeout in wait_for_transaction_receipt is good practice
            w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)

            print(f"Logged packet features to blockchain. Tx hash: {tx_hash.hex()}")
        except Exception as e:
            print(f"An error occurred while logging the packet: {e}")
            print("Please check the account, private key, gas settings, and contract logic.")
    else:
        print("Skipping packet logging due to previous errors creating the contract instance.")
else:
    print("Skipping packet logging as the connection to Ganache failed.")