from eth_account import Account
import json

def create_bsc_wallets(number_of_wallets):
    wallets = []
    for _ in range(number_of_wallets):
        acct = Account.create()
        private_key = acct._private_key.hex()
        address = acct.address
        wallets.append({'private_key': private_key, 'address': address})
    return wallets

def save_wallets_to_json(wallets, filename='wallets.json'):
    with open(filename, 'w') as f:
        json.dump(wallets, f, indent=4)

def extract_wallet_addresses(json_file, output_file='wallet_addresses.txt'):
    with open(json_file, 'r') as file:
        data = json.load(file)
    with open(output_file, 'w') as file:
        for wallet in data:
            file.write(wallet['address'] + '\n')

def banner():
    print("""
EVM Wallet Generator
          
Github: https://github.com/Tnodes
    """)

def main():
    banner()
    while True:
        print("Choose an option:")
        print("1. Generate EVM Wallet")
        print("2. Merge All EVM Wallets")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            number_of_wallets = int(input("Enter the number of wallets to create: "))
            filename = input("Enter the filename (with ext. .json) to save wallets or press Enter to use default: ")
            if filename.strip() == '':
                filename = 'wallets.json'
            wallets = create_bsc_wallets(number_of_wallets)
            save_wallets_to_json(wallets, filename)
            print(f"Wallets successfully created and saved in {filename}")

        elif choice == '2':
            json_file = input("Enter the JSON filename (with ext. .json) to extract or press Enter to use default: ")
            if json_file.strip() == '':
                json_file = 'wallets.json'
            output_file = input("Enter the output filename for addresses or press Enter to use default: ")
            if output_file.strip() == '':
                output_file = 'wallet_addresses.txt'  # Default output filename
            extract_wallet_addresses(json_file, output_file)
            print(f"Wallet addresses successfully extracted and saved in {output_file}")
        
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
