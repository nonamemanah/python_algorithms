from api.openexchangerates import OpenExchangeRatesApi
import sys


def main():
    api = OpenExchangeRatesApi()
    api.load()

    sorted_currency = api.sorted_currency
    for item in sorted_currency:
        print(item)

    print(f'Количество ссылок на объект: {sys.getrefcount(sorted_currency)}')


if __name__ == "__main__":
    main()
