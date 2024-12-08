# README: Date Reformatting Script

## Overview
This Python script reads an Excel file, reformats the dates in the **"Created Date"** or **"DateColumnName"** column to a specific format, and saves the updated data to a new Excel file. The script handles dates in two formats:

1. **DD-MM-YYYY**: Converts to MM-DD-YYYY format.
2. **MM/DD/YYYY**: Converts to DD-MM-YYYY format.

If a date cannot be parsed, the script retains the original value.

---

## Prerequisites

### System Requirements
- Python 3.x installed on your system.

### Required Libraries
This script uses the following Python libraries:
- **pandas**: For data manipulation.
- **openpyxl**: For Excel file handling.

Install these libraries using:
```bash
pip install pandas openpyxl
