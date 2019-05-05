from api.openexchangerates import OpenExchangeRatesApi


def main():
    api = OpenExchangeRatesApi()
    api.load_currencies()

    for item in api.currencies:
        print(item)


if __name__ == "__main__":
    main()
