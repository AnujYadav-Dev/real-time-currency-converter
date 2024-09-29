import requests

# Function to fetch real-time exchange rates
def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    
    # Check if the response is valid
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rate']
    else:
        return None

# Function to perform the currency conversion
def convert_currency(api_key, base_currency, target_currency, amount):
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
    
    if exchange_rate:
        converted_amount = amount * exchange_rate
        return converted_amount, exchange_rate
    else:
        return None, None

# List of supported currencies
currencies = {
    'INR': 'Indian Rupee',
    'USD': 'United States Dollar',
    'EUR': 'Euro',
    'GBP': 'British Pound',
    'JPY': 'Japanese Yen',
    'AUD': 'Australian Dollar',
    'CAD': 'Canadian Dollar',
    'CHF': 'Swiss Franc',
    'CNY': 'Chinese Yuan',
    'SEK': 'Swedish Krona',
    'NZD': 'New Zealand Dollar'
}

# Main Program
if __name__ == "__main__":
    api_key = "" # Your API Key
    
    # Display available currencies
    print("Available currencies:")
    for code, name in currencies.items():
        print(f"{code}: {name}")

    # User inputs
    base_currency = input("Enter the base currency code (e.g., INR): ").upper()
    if base_currency not in currencies:
        print("Invalid base currency code.")
        exit()

    target_currency = input("Enter the target currency code (e.g., USD): ").upper()
    if target_currency not in currencies:
        print("Invalid target currency code.")
        exit()
    
    amount = float(input(f"Enter the amount in {base_currency}: "))

    # Conversion
    converted_amount, exchange_rate = convert_currency(api_key, base_currency, target_currency, amount)
    
    if converted_amount:
        print(f"\n{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        print(f"Exchange Rate: 1 {base_currency} = {exchange_rate:.2f} {target_currency}")
    else:
        print("Failed to retrieve exchange rate. Please try again.")
