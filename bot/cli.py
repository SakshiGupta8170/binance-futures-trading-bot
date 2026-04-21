import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    setup_logging()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        client = BinanceClient(API_KEY, API_SECRET).get_client()

        print("Order Summary:", vars(args))

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        if response:
            print("Order Success:", response)
        else:
            print("Order Failed")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
