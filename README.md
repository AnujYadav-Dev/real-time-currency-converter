
# Currency Converter

A Python-based currency converter that allows users to convert amounts between different currencies using real-time exchange rates. This tool supports a selection of popular currencies, including the Indian Rupee (INR), and provides a user-friendly command-line interface.

## Features

- **Real-Time Exchange Rates**: Retrieves the latest exchange rates from a reliable API.
- **Interactive Currency Selection**: Choose from a list of top global currencies and the Indian Rupee (INR).
- **Simple and Clear Output**: Displays the converted amount and the exchange rate.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library for HTTP requests

You can install the `requests` library using pip:

```bash
pip install requests
```

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AnujYadav-Dev/currency-converter.git
   cd currency-converter
   ```

2. **Add Your API Key**

   Open `currency_converter.py` and set your own API key from [ExchangeRate-API](https://www.exchangerate-api.com/).

3. **Run the Application**

   ```bash
   python currency_converter.py
   ```

4. **Follow the Prompts**

   - Enter the base currency code (e.g., INR).
   - Enter the target currency code (e.g., USD).
   - Enter the amount you want to convert.

## Example Usage

```
Available currencies:
INR: Indian Rupee
USD: United States Dollar
EUR: Euro
GBP: British Pound
JPY: Japanese Yen
AUD: Australian Dollar
CAD: Canadian Dollar
CHF: Swiss Franc
CNY: Chinese Yuan
SEK: Swedish Krona
NZD: New Zealand Dollar


Enter the base currency code (e.g., INR): USD
Enter the target currency code (e.g., USD): EUR
Enter the amount in USD: 100

100 USD = 84.50 EUR
Exchange Rate: 1 USD = 0.8450 EUR
```

## Supported Currencies

- INR: Indian Rupee
- USD: United States Dollar
- EUR: Euro
- GBP: British Pound
- JPY: Japanese Yen
- AUD: Australian Dollar
- CAD: Canadian Dollar
- CHF: Swiss Franc
- CNY: Chinese Yuan
- SEK: Swedish Krona
- NZD: New Zealand Dollar

## Contributing

Contributions are welcome! Please open issues or submit pull requests to improve the project.

## Happy Coding 
