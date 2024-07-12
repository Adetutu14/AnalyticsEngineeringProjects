import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from datetime import datetime

#Database credentials
db_user_name = 'postgres'
db_password = 'Engrtutu14'
host = 'localhost'
port = 5432
db_name = 'stock_exchange2'


#Data extraction layer
# This code is not correct it is repeating the table over again 
def extract_data():
    count = 0
    pages = 1
    num_pages = 2
    df = []
    url = 'https://afx.kwayisi.org/ngx/'

    while count <= pages:
        pages_url = f'{url}?page={pages}'
        scrap_data = requests.get(pages_url)
        scrap_data = scrap_data.content
        html_data = BeautifulSoup(scrap_data, 'lxml')  # Using lxml parser
        tables = html_data.find_all('table')

        if not tables:
            break
        stock_data = str(tables[3])  # Selecting the fourth table
        dfs = pd.read_html(stock_data)
        df.append(dfs[0])  # Append the DataFrame to the list
        pages += 1
        count += num_pages
        
    final_df = pd.concat(df, axis = 0)
    # print(final_df)
    # print(final_df.shape)
    final_df.to_csv('extraction/stock_data2.csv', index = False)
    print('Data has been successfully written to a csv file')

#extract_data()

# Data Transform layer
def transform_data():
    data = pd.read_csv('extraction/stock_data2.csv') #Read the csv file
    data = data.rename ({'Ticker':'ticker', 'Name':'name', 'Volume':'volume', 'Price':'price', 'Change': 'change'}, axis = 1) #axis aids it in lower case
    data['date'] = datetime.today().date() #.date() extract only the date and removes the time
    mean_vol = data['volume'].mean()
    # print(mean_vol)
    data['volume'] = data['volume'].fillna(mean_vol)
    # print(data.head(10))
    # data.to_csv('transform/transformed_stock_data2.csv', index = False)
    # print('Data has been transformed to csv successfully')

# transform_data()


# Data loading layer
# Here we load in the stock_data into our postgresql after creating our database name
def load_to_dbase():
    data = pd.read_csv('transform/transformed_stock_data2.csv') #Read the csv file
    engine = create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
    data.to_sql('stock_data2', con = engine, if_exists= 'replace', index = False)
    print('Data has been successfully loaded into postgresql database')

#load_to_dbase()


#extract_data()
#transform_data()
#load_to_dbase()








