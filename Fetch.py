import requests
import pyodbc
import pandas as pd
    
API_KEY = 'API KEY'
symbol = 'AAPL'
url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={API_KEY}&serietype=line"

response = requests.get(url)
data = response.json()

if 'historical' not in data:
    print('Warning: not historical in data')
    print(data)
    exit()

df = pd.DataFrame(data['historical'])
print('First 5 rows:')
print(df.head())

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LAPTOP-77CU778B\\SQLEXPRESS;'
    'DATABASE=FinanceDB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

for idx, row in df.iterrows():
    cursor.execute(
        'INSERT INTO StockPrices(Symbol, Date, ClosePrice) VALUES(?, ?, ?)',
        (symbol, row['date'], row['close'])
    )
conn.commit()
conn.close()

print('Data save in MSSQL')