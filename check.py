import blockcypher
from moneywagon import AddressBalance

def balance(addr):
    try:
        total = blockcypher.get_total_balance(addr)
        print('Balance is ' + str(total))
    except:
        total = AddressBalance().action('btc', addr)
        print('Balance is ' + str(total))

def main():
    file_path = "wallets.txt"

    try:
        with open(file_path, 'r') as file:
            addresses = file.readlines()
            addresses = [addr.strip() for addr in addresses]

        for addr in addresses:
            print(f"\nChecking balance for address: {addr}")
            balance(addr)
            
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
