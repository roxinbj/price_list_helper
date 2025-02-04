import argparse
from price_list_helper.commands import clear, list_types
from price_list_helper.commands.add import handle_add, parse_item_type
#from price_list_helper.utils.helpers import SensorType

def main():
    print("Hello")

    parser = argparse.ArgumentParser(description="Price List Helper CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add an item to the list")
    add_parser.add_argument(
        "type", 
        type=parse_item_type, 
        help="Type of the item (e.g., dragino-ps-lb, banana, cherry)"
    )
    add_parser.add_argument("qty", type=int, help="Quantity of the item")
    add_parser.add_argument("price",type=float,help="Cost to company price per piece of current order (NAD)")
    add_parser.set_defaults(func=handle_add)

    # Clear command
    clear_parser = subparsers.add_parser("clear", help="Clear the list")
    clear_parser.set_defaults(func=clear.handle_clear)

    # List-types command
    list_types_parser = subparsers.add_parser("list-types", help="List all available item types")
    list_types_parser.set_defaults(func=list_types.handle_list_types)
    
    # Parse and execute
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
