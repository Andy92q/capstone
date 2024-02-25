import pandas as pd
import os
import platform


def openExcelFile(classNum):
    """This function opens the excel file from python

    Args:
        classNum (str): eg. "1"

    Returns:
        excel opened  
    """
    # Specify the path to your Excel file
    excel_file = "./excel/"+classNum+".xlsx"
    # Use pandas to read the Excel file
    dp = pd.read_excel(excel_file)
    # Display the DataFrame (optional)
    print(dp)

    # Open the Excel file in the default application
    system_name = platform.system().lower()

    if system_name == 'darwin':  # macOS
        os.system(f'open "{excel_file}"')
    elif system_name == 'linux':  # Linux
        # Try xdg-open first, then gnome-open
        os.system(f'xdg-open "{excel_file}"') or os.system(f'gnome-open "{excel_file}"')
    elif system_name == 'windows':
        # On Windows, the original start command should work
        os.system(f'start excel "{excel_file}"')
    else:
        print(f"Unsupported operating system: {system_name}")