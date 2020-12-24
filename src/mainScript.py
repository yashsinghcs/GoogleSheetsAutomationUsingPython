# importing the required libraries
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('your jason file here', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('your sheets name')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)
# get the total number of columns
print(sheet_instance.col_count)

# get all the records of the data
records_data = sheet_instance.get_all_records()

# add data to sheets
sheet_instance.insert_rows([["row to add"],["row to add"]],"index here")