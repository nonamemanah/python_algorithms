from api.openexchangerates import OpenExchangeRatesApi


def main():
    api = OpenExchangeRatesApi()
    api.load()

    for item in api.sorted_currency:
        print(item)


if __name__ == "__main__":
    main()
