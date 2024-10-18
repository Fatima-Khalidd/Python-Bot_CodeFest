import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES =["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID="1xFukNASy7VFPNV3b5cKHHgTDlIaFpMyPx4WZ-AXOgWg"

def main():
    credentials=None
    if os.path.exists("token.json"):
        credentials=Credentials.from_authorized_user_file(token.json,SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else: 
                flow= InstalledAppFlow.from_client_secrets_file("credentials.json",SCOPES)
                credentials=flow.run_local_server(port=0)
                #credentials=flow.run_console()
                with open("token.json","w") as token:
                    token.write(credentials.to_json())
            try:
                service=build("sheets","v4",credentials=credentials)
                sheets=service.spreadsheets()
                data=f"Sheet1! A1:A6"
                result=sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=data).execute()
                values=result.get("values",[])
                
                for row in values:
                    print(row)
            except HttpError:
                print("error")

import os

if os.getenv("DISPLAY") is None:
    print("Headless environment detected: No GUI available.")
else:
    print("GUI environment detected.")

if __name__ =="__main__":
    main()



    