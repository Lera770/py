import requests
from datetime import datetime

def get_exchange_rate(currency_code_a=840, currency_code_b=980):
    """
    Get the currency rate from Monobank API.
    By defauit: USD (840) to  UAH (980)
    
    List of currency codes:
    USD - 840 (Dollar)
    EUR - 978 (Euro)
    UAH - 980 (Hryvnia)
    PLN - 985 (Zloty)
    """
    url = "https://api.monobank.ua/bank/currency"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
    
        for rate in data:
            if rate["currencyCodeA"] == currency_code_a and rate["currencyCodeB"] == currency_code_b:
                buy_rate = rate.get("rateBuy", "N/A")
                sell_rate = rate.get("rateSell", "N/A")
                date_updated = datetime.fromtimestamp(rate["date"]).strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"Course {currency_code_a} → {currency_code_b}:")
                print(f"  Purchase: {buy_rate}")
                print(f"  Sale: {sell_rate}")
                print(f"  Update: {date_updated}")
                return
        
        print("Currency pair not found.")
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Error: {e}")

get_exchange_rate(840, 980)
