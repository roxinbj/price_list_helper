import gspread
from enum import Enum

# Define the enum for Item Types
class SensorType(Enum):
    DRAGINO_PSLB = "ps-lb" # Analog Reader
    DRAGINO_DDS75 = "dds75" # Ultrasonics
    DRAGINO_LT_22222 = "lt-22222" # Controller
    RAK_7240V2_4G = "7240v2-4g" # Gateway 4G
    RAK_7240V2 = "7240v2" # Gateway Ethernet
    MILESIGHT_UC300 = "uc300" # UC300 Controller Lora
    MILESIGHT_UC300_4G = "uc300-4g" # UC300 Controller 4G
    MILESIGHT_EM300 = "em300" # Pulse Counter
    CT100 = "ct100" # Controller


sheet_name = "Copy of Sigmotec Inventory"

# Authenticate and initialize Google Sheets client
def get_sheets_client():
    """
    Authenticate using a service account and return a Google Sheets client.
    Ensure the service account JSON file is properly set up.
    """
    service_account = gspread.service_account()
    return service_account

def clear_sheet():
    """
    Clear all rows in the specified sheet.
    """
    client = get_sheets_client()
    sheet = client.open(sheet_name)
    worksheet = sheet.worksheet("Check In: QR Code Print")
    worksheet.clear()
    print(f"Cleared all rows in sheet: {sheet_name} -> Check In: QR Code Print")

def add_type_qty(item_type, qty):
    """
    Add <qty> items of <item_type> to the sheet "Check In: QR Code Print".

    Args:
        sheet_name (str): The name of the Google Sheet.
        item_type (SensorType): The type of the item to add.
        qty (int): The quantity to add.
    """
    client = get_sheets_client()

    # Open the sheets
    inventory_status_sheet = client.open(sheet_name).worksheet("Inventory Status")
    check_in_sheet = client.open(sheet_name).worksheet("Check In: QR Code Print")
    check_out_sheet = client.open(sheet_name).worksheet("Check Out")

    # Fetch all data from Inventory Status sheet
    inventory_data = inventory_status_sheet.col_values(1)  # Column A
    check_in_data = check_in_sheet.col_values(1) # Column A
    check_out_data = check_out_sheet.col_values(2) # Column B

    # Find the last number for the given item type
    # In Inventory Sheet, Check in sheet and Checkout sheet
    max_number = 0
    for row in inventory_data:
        if row.startswith(f"{item_type.value}_"):
            number_part = int(row.split("_")[1])
            max_number = max(max_number, number_part)
    
    for row in check_in_data:
        if row.startswith(f"{item_type.value}_"):
            number_part = int(row.split("_")[1])
            max_number = max(max_number, number_part)
    
    for row in check_out_data:
        if row.startswith(f"{item_type.value}_"):
            number_part = int(row.split("_")[1])
            max_number = max(max_number, number_part)

    # Generate new rows for the Check In: QR Code Print sheet
    new_rows = [
        f"{item_type.value}_{str(max_number + i).zfill(4)}" for i in range(1, qty + 1)
    ]

    # Append new rows to the Check In sheet
    check_in_sheet.append_rows([[row] for row in new_rows], value_input_option="USER_ENTERED")

    print(f"Added {qty} items of type '{item_type.value}' to Check In sheet.")

# Example usage
if __name__ == "__main__":
    # Clear all rows in Check In sheet
    #sheet_name = "Copy of Sigmotec Inventory"
    print("HElüp")
    #clear_sheet(sheet_name)

    
    # Add 3 apples to the Check In sheet
    add_type_qty(sheet_name,SensorType.DRAGINO_PSLB, 3)
