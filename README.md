# Wallet Balance Checker

This Python script enables users to quickly check the balance of Bitcoin (BTC) wallets. It utilizes the BlockCypher and Moneywagon APIs to fetch wallet balances. The script reads addresses from a file named `wallets.txt`, and then iterates through each address, printing out its balance.

## Prerequisites

Ensure you have Python 3.x installed on your system.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies using pip:
    ```bash
    pip install blockcypher moneywagon
    ```

## Usage

1. Create a text file named `wallets.txt` in the same directory as the script.
2. Add Bitcoin wallet addresses, each on a new line, to the `wallets.txt` file.
3. Run the script using the following command:
    ```bash
    python check.py
    ```
4. The script will output the balance of each wallet address listed in the `wallets.txt` file.

## Error Handling

- If the `wallets.txt` file is not found, the script will display an error message.
- If any other error occurs during execution, the script will print an error message with details.


