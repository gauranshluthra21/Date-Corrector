import pandas as pd

# Load the Excel file
file_path = r"Your_FileHere.xlsx"
df = pd.read_excel(file_path)

# Function to reformat the date
def reformat_date(date_str):
    try:
        # Try to parse the date assuming DD-MM-YYYY format
        date = pd.to_datetime(date_str, format='%d-%m-%Y', errors='coerce')
        if pd.notnull(date):
            return date.strftime('%m-%d-%Y')
    except ValueError:
        pass
    
    try:
        # Try to parse the date assuming MM/DD/YYYY format
        date = pd.to_datetime(date_str, format='%m/%d/%Y', errors='coerce')
        if pd.notnull(date):
            return date.strftime('%d-%m-%Y')
    except ValueError:
        pass
    
    # If parsing fails, return the original string
    return date_str

# Apply the function to the 'Created Date' column
df['Created Date'] = df['Created Date'].apply(reformat_date)

# Save the updated DataFrame to a new Excel file
output_file_path = r"UpdatedFileHere.Xlsx"
df.to_excel(output_file_path, index=False)

print(f"Updated file saved as {output_file_path}")
