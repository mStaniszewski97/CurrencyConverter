from datetime import date

import constants
from client import Client


def collect_currencies():
    currencies = []
    n = int(input("How many currencies codes would you like to enter?"))
    for i in range(0, n):
        currency_code = input("Enter currency code: ")
        if currency_code in constants.CURRENCY_LIST.keys():
            currencies.append(currency_code)
        else:
            print("Wrong currency code!!!")
    return currencies


def get_base_currency():
    base_currency = input("Enter base currency code: ")
    if base_currency not in constants.CURRENCY_LIST.keys():
        raise AttributeError("Wrong base currency code, closing the program")
    else:
        return base_currency


def main():
    request_client = Client(constants.API_KEY, constants.API_URL)
    print("Welcome to currency converter app")
    print("Available currencies are:")

    for code, country in constants.CURRENCY_LIST.items():
        print(code, country)
    print("Available endpoints:", "1-/status", "2-/latest", "3-/historical", "4-/currencies", sep='\n')

    endpoint = input("Enter: [1,2,3,4]")

    if endpoint == "1":
        print(request_client.status())
    elif endpoint == "2":
        print(request_client.latest(get_base_currency(), collect_currencies()))
    elif endpoint == "3":
        first_day_of_the_year = date.today().replace(month=1, day=1)
        print(request_client.historical(first_day_of_the_year, get_base_currency(), collect_currencies()))
    elif endpoint == "4":
        print(request_client.currencies(collect_currencies()))
    else:
        raise Exception("Wrong option was selected, closing the program")


if __name__ == "__main__":
    main()
