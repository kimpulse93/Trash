from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# from gglshts import get_data
import numpy as np
import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1x7LIKoYOh4MplxihQr3lCb5FPLtHLx7pkOZxbgefpGc'
SAMPLE_RANGE_NAME = "'Данные'!A:J"


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    # print(values)
    return values



if __name__ == '__main__':
    #График Кол-ва решенных на 1,2 ЛП
    data = main()
    # Преобразование в DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])
    # Выборка столбцов df
    ds1 = df[['Номер','Дата решения','ЛП']]
    # Создание сводной таблицы1
    dg1 = ds1.pivot_table(index='Дата решения', columns='ЛП', values='Номер', aggfunc='count')# колво решенных на 1 2лп
    print(dg1)
    # a = dg1
    # Добавление столбца процентов
    # a['3'] = a['1']/(a['1']+a['2'])*100
    # dg2 = a[['3']]
    #plt.figure(figsize=(20, 8))
    #
    # plt.plot(dg1, color='green', marker='o', linestyle='--', markerfacecolor='blue')
    #
    #
    #
    # #plt.plot(dg2, color='green', marker='o', linestyle='--', markerfacecolor='blue')
    # plt.show()


    ds2 = df[['Номер','Группа поддержки','ЛП']]

    dg2 = ds2.pivot_table(index='Группа поддержки', columns='ЛП', values='Номер', aggfunc='count')
    print(dg2)
    plt.hist(dg2, color='green', marker='o', linestyle='--', markerfacecolor='blue')
    plt.show()







