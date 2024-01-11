import pandas as pd
import json
import os
import platform


excel_file_path = 'test.xlsx'
# Read the modified Excel file into a DataFrame
# modified_df = pd.read_excel(excel_file_path, skiprows=1, skip_cols=1)


# modified_df = pd.read_excel("test.xlsx", skip_cols=[1], skiprows=[0])
skip_cols='A'
modified_df = pd.read_excel(excel_file_path, skiprows=0, usecols=lambda x: x not in skip_cols)

modified_array = [row.tolist() for _, row in modified_df.iterrows()]




# Overwrite the middle.txt file with the updated array
with open("middle.txt", "w") as f:
    json.dump(modified_array, f)

# Display the updated array (optional)
print(modified_array)

# Open the Excel file in the default application
system_name = platform.system().lower()

if system_name == 'darwin':  # macOS
    os.system(f'open "{excel_file_path}"')
elif system_name == 'linux':  # Linux
    # Try xdg-open first, then gnome-open
    os.system(f'xdg-open "{excel_file_path}"') or os.system(f'gnome-open "{excel_file_path}"')
elif system_name == 'windows':
    # On Windows, the original start command should work
    os.system(f'start excel "{excel_file_path}"')
else:
    print(f"Unsupported operating system: {system_name}")
