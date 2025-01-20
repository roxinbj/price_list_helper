import gspread
from enum import Enum

# Define the enum for Item Types
class SensorType(Enum):
    APPLE = "apple"
    BANANA = "banana"
    CHERRY = "cherry"

# Authenticate and initialize Google Sheets client
def get_sheets_client():
    """
    Authenticate using a service account and return a Google Sheets client.
    Ensure the service account JSON file is properly set up.
    """
    service_account = gspread.service_account()
    return service_account

def clear_sheet(sheet_name):
    """
    Clear all rows in the specified sheet.
    """
    client = get_sheets_client()
    sheet = client.open(sheet_name)
    worksheet = sheet.worksheet("Check In: QR Code Print")
    worksheet.clear()
    print(f"Cleared all rows in sheet: {sheet_name} -> Check In: QR Code Print")

def add_type_qty(sheet_name,item_type, qty):
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

    # Fetch all data from Inventory Status sheet
    inventory_data = inventory_status_sheet.col_values(1)  # Column A

    # Find the last number for the given item type
    max_number = 0
    for row in inventory_data:
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
    sheet_name = "Copy of Sigmotec Inventory"
    print("HElüp")
    clear_sheet(sheet_name)

    
    # Add 3 apples to the Check In sheet
    add_type_qty(sheet_name,SensorType.APPLE, 3)
