
import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://open.er-api.com/v6/latest/"

    def get_exchange_rates(self, base_currency):
        url = f"{self.base_url}{base_currency.upper()}?apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data.get('rates', {})

    def convert(self, amount, from_currency, to_currency):
        rates = self.get_exchange_rates(from_currency)
        if not rates:
            print(f"Failed to fetch exchange rates for {from_currency}")
            return None

        exchange_rate = rates.get(to_currency.upper())
        if exchange_rate is None:
            print(f"Exchange rate not available for {to_currency}")
            return None

        converted_amount = amount * exchange_rate
        return converted_amount

# Example usage:
api_key = "03e034c3cee372c6fa924f5d"
converter = CurrencyConverter(api_key)


from_currency = input("Enter the source currency code (e.g., USD): ").upper()
to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
amount = float(input("Enter the amount to convert: "))

result = converter.convert(amount, from_currency, to_currency)
if result is not None:
    print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
