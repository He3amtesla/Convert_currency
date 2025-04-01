# Streamlit Currency Converter

A simple web application built with Streamlit that allows users to convert amounts between various currencies using real-time exchange rates.

## Description

This tool provides a user-friendly interface to:
* Select a base currency.
* Select a target currency.
* Enter an amount to convert.
* View the converted amount based on the latest available exchange rates.
* See when the exchange rate data was last updated.

The application utilizes the [ExchangeRate-API](https://www.exchangerate-api.com/) to fetch currency conversion data.

## Features

* **Real-time Conversion:** Uses up-to-date exchange rates from an external API.
* **Wide Currency Support:** Supports a large list of international currencies (dynamically updated based on API response).
* **Caching:** Caches API results for 3 hours to improve performance and reduce API calls.
* **User-Friendly Interface:** Simple and interactive UI built with Streamlit.
* **Displays Last Update Time:** Shows users the freshness of the exchange rate data.

## Project Structure

```
├── src/
│   ├── app.py             # Main Streamlit application script
│   ├── convert_currency.py # Handles API calls, caching, and conversion logic
│   ├── currency.py        # Stores the list of available currency codes (dynamically updated)
└── README.md          # This file
```

## Requirements

* Python 3.x
* `streamlit`
* `requests`
* `cachetools`

## Installation

1.  **Clone the repository (or download the files):**
    ```bash
    # If using git
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```
2.  **Install the required Python packages:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install streamlit requests cachetools
    ```

## Usage

1.  **Navigate to the project directory** (where the `src` folder is located) in your terminal.
2.  **Run the Streamlit application:**
    ```bash
    streamlit run src/app.py
    ```
3.  Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).
4.  Use the dropdown menus to select the 'From Currency' (base) and 'To Currency' (target).
5.  Enter the amount you wish to convert in the 'Enter amount' field.
6.  The converted amount and the exchange rate's last update time will be displayed automatically.

## How it Works

* **`app.py`**: Sets up the Streamlit interface, takes user input (currencies and amount), calls the conversion functions, and displays the results.
* **`convert_currency.py`**:
    * `get_exchange_money()`: Fetches the latest exchange rates for a given base currency from `v6.exchangerate-api.com` using the `requests` library. It includes an API key directly in the code. It uses `cachetools.TTLCache` to cache the response for 3 hours. It also dynamically updates the `src/currency.py` file with the list of available currencies from the API response.
    * `convert_currency()`: Performs the simple multiplication to convert the amount based on the fetched rate.
* **`currency.py`**: Initially contains a list of currency codes, but this file gets overwritten by `convert_currency.py` with the latest list whenever `get_exchange_money` successfully fetches data.
