import streamlit as st
from currency import currencyes
from convert_currency import get_exchange_money, convert_currency

st.markdown(
    "<h1 style='display: flex; align-items: center;'>" 
    "<img src='https://www.shutterstock.com/image-vector/currency-exchange-money-conversion-euro-600nw-1919947535.jpg' width='80' style='margin-right: 10px;'>" 
    "Currency Converter</h1>", 
    unsafe_allow_html=True
)#This piece of code <helped by chatgptt>

st.markdown("""
This tool allows you to instantly convert amounts between different currencies :earth_africa::sparkles:. Enter the amount and choose the currencies to see the result.
            """)
base_currency = st.selectbox("From Currncy (base): ",currencyes)
target_currency = st.selectbox("From Currncy (target): ",currencyes)

total_number = st.number_input("Enter amount: ", min_value = 0.0, value = 10.0) #هردو مقدار باید دیتااستراکچر برابری داشته باشند

if total_number > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_money(base_currency, target_currency)
    
    if exchange_rate:
        convert_amount = convert_currency(exchange_rate, total_number)
        st.success(f"✅Exchange Rate:{convert_amount:.4f}") #:.4f نشان دادن با 4 رقمت اعشاری
        
        col1, col2, col3 = st.columns(3)
        col1.metric(label = "Base Currncey", value = f"{total_number:.2f} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0; color: brown;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label = "Target Currncey", value = f"{convert_amount:.2f} {target_currency}")
    else:
        st.error("Error fetching exchange rate.")
st.markdown("___")    
st.markdown("""### About This Tool:
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
The conversion updates automatically as you input the amount or change the currency.
Enjoy seamless currency conversion without the need to press a button!""")