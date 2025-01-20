from price_list_helper.utils.helpers import SensorType

def handle_list_types(args):
    print("Sensor types are")
    for item in SensorType:
        print(f"- {item.value}")