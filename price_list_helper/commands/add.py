import argparse
from price_list_helper.utils.types import SensorType


def parse_item_type(value):
    try:
        return SensorType(value)
    except ValueError:
        valid_values = ", ".join([item.value for item in SensorType])
        raise argparse.ArgumentTypeError(
            f"Invalid type '{value}'. Must be one of: {valid_values}"
        )


def handle_add(args):

    item_type = args.type
    qty = args.qty
    # Logic to add the item
    print(f"Adding {qty} of type '{item_type}' to the list.")
