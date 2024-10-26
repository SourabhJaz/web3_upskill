# Solana Wallet CLI
=====================

A simple command-line interface (CLI) for creating and managing Solana wallets.

## Features

* Create a new Solana wallet with a unique public and private key pair
* Get the balance of a Solana wallet by its public key

## Requirements

* Python 3.7+
* `solders` library for Solana keypair and pubkey management
* `solana.rpc.async_api` library for interacting with the Solana blockchain

## Usage

1. Clone this repository and navigate to the project directory.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the script using `python wallet.py`.
4. Follow the menu prompts to create a new wallet, get the balance of an existing wallet, or exit the program.

## Creating a Wallet

* Select option 1 from the menu to create a new wallet.
* The script will generate a new keypair and display the public key (wallet ID) and private key.

## Getting Balance

* Select option 2 from the menu to get the balance of an existing wallet.
* Enter the public key (wallet ID) of the wallet you want to check.
* The script will query the Solana blockchain and display the wallet balance.

## Notes

* This script uses the Solana Devnet API by default. You can modify the `AsyncClient` URL to use a different Solana cluster (e.g., Mainnet).
* Keep your private keys safe and secure! This script displays the private key for demonstration purposes only.

## Contributing

Contributions are welcome! If you'd like to add new features or improve the existing code, please submit a pull request.
