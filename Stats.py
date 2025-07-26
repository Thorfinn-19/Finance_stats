import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LAPTOP-77CU778B\\SQLEXPRESS;'
    'DATABASE=FinanceDB;'
    'Trusted_Connection=yes;'
)

query = "SELECT Date, ClosePrice FROM StockPrices WHERE Symbol='AAPL' ORDER BY Date;"
df = pd.read_sql(query, conn)
conn.close()

print(df.head())
print('Átlagos záróár: ',df['ClosePrice'].mean())
#plt.plot(pd.to_datetime(df['Date']), df['ClosePrice'])
plt.plot(df['Date'], df['ClosePrice'])
plt.title('AAPL záróár alakulása')
plt.xlabel('Dátum')
plt.ylabel('Záróár')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()