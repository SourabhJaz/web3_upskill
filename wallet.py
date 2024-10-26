from solders.keypair import Keypair
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
import asyncio

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Create Wallet")
        print("2. Get Balance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Creating a wallet...")
            keypair = Keypair()
            print("Wallet created successfully.")
            print("Public key/Wallet id:", keypair.pubkey())
            print("Private key:", keypair.secret())
        elif choice == '2':
          wallet_id = input("Enter wallet id: ")
          client = AsyncClient("https://api.devnet.solana.com")
          async def get_balance():
            pubkey = Pubkey.from_string(wallet_id)
            res = await client.get_balance(pubkey)
            return res
          res = asyncio.run(get_balance())
          print(res)
        else:
            print("Exiting...")
            break