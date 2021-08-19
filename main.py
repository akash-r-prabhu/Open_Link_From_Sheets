from googleapiclient.discovery import build
from google.oauth2 import service_account
import webbrowser
import time
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# The ID spreadsheet.

# Enter your spreadsheet id inside the below quotes
SAMPLE_SPREADSHEET_ID = 'spreadsheet_id' 

service = build('sheets', 'v4', credentials=creds)
# Call the Sheets API
sheet = service.spreadsheets()
c_time=time.time()
i=0
# i=int(input("enter the value"))-1
result1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range="Sheet1!B:Z").execute()

i=int(result1['values'][0][0])
while(1==1):
    if(int(time.time())==int(c_time+10)):
        c_time=c_time+10
        # test

        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range="A1:C100").execute()

        values = result.get('values', [])
        # gg
        aoa=[[str(i)]]
        what_to_insert=aoa
        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="Sheet1!B:Z", valueInputOption="USER_ENTERED", body={"values":what_to_insert}).execute()

        # test
        s=list(values)
        if i<len(s):
            c=str(s[i][0]).strip()
            if(c is not None):
                webbrowser.open(c)    
            i+=1
