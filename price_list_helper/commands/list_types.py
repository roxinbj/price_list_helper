from price_list_helper.utils.types import SensorType

def handle_list_types(args):
    print("Sensor types are")
    for item in SensorType:
        print(f"- {item.value}")