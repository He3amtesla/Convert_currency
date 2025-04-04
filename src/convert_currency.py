import requests
from cachetools import cached, TTLCache

ttl_cache =TTLCache(maxsize=299, ttl= 60*60*3)

@cached(ttl_cache)
def get_exchange_money(base_money: str, target_money: str) -> float:
    response = requests.get(f"https://v6.exchangerate-api.com/v6/94279738aa864d272c0be4e0/latest/{base_money}")
    if response.status_code != 200:
        return None
    
    with open("currency.py",'w') as file:
        l = list(response.json()["conversion_rates"].keys())
        file.write("currencyes =" + str(l))
        
    time_last_update = response.json()["time_last_update_utc"]
    rate = response.json()["conversion_rates"][target_money]
    
    return rate, time_last_update



def convert_currency(amount_of_currency: float, total_number: float) -> float:
    return (amount_of_currency * total_number)


if __name__ == "__main__":
    base_money = input("Enter your base money: ")
    target_money = input("Enter Target money: ")
    total_number = float(input("Enter Total Number Target money: "))
    
    amount_of_currency_of_currency, time = get_exchange_money(base_money, target_money)
    cc = convert_currency(amount_of_currency_of_currency, total_number)
    print((cc))