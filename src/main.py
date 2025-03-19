import requests


def get_exchange_money(base_money: str, target_money: str) -> float:
    response = requests.get(f"https://v6.exchangerate-api.com/v6/94279738aa864d272c0be4e0/latest/{base_money}")
    return response.json()["conversion_rates"][target_money]

def convert_currency(amount: float, total_number: float) -> float:
    return amount * total_number

if __name__ == "__main__":
    base_money = input("Enter your base money: ")
    target_money = input("Enter Target money: ")
    total_number = float(input("Enter Total Number Target money: "))
    
    amount = get_exchange_money(base_money, target_money)
    cc = convert_currency((amount), total_number)
    print(cc)