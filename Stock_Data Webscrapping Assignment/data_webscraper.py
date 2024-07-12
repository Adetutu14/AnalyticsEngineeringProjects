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
db_name = 'stock_exchange'


# Data Extraction Layer
# Here we extract the 1st page of the table on the webpage
def extract_data1():
    url = 'https://afx.kwayisi.org/ngx/'
    scrap_data = requests.get(url)
    scrap_data = scrap_data.content
    html_data = BeautifulSoup(scrap_data ,'lxml') #parse
    stock_data1 = str(html_data.find_all('table'))
    df1 = pd.read_html(stock_data1)
    print(df1[3])
    return df1[3]
    
# extract_data1()


# Here we extract the 2nd page of the table on the web page
def extract_data2():
    url = 'https://afx.kwayisi.org/ngx/?page=2'
    scrap_data = requests.get(url)
    scrap_data = scrap_data.content
    html_data = BeautifulSoup(scrap_data ,'lxml') #parse
    stock_data2 = str(html_data.find_all('table'))
    df2 = pd.read_html(stock_data2)
    print(df2[3])
    return df2[3]

# extract_data2()


# Here we combine the table extracted from 1st page and 2nd page using pd.concat
def combine_data():
    df1 = extract_data1()
    df2 = extract_data2()
    final_df = pd.concat( [df1, df2], axis = 0 )
    #print(final_df)
    final_df.to_csv('extraction/stock_data.csv', index = False)
    print('Data Successfully written to a csv file')

# combine_data()

# Data load transformation layer
# Here we transform and load the data with all conditions included
def transform_data():
    data = pd.read_csv('extraction/stock_data.csv') #Read the csv file
    data = data.rename ({'Ticker':'ticker', 'Name':'name', 'Volume':'volume', 'Price':'price', 'Change': 'change'}, axis = 1) #axis aids it in lower case
    data['date'] = datetime.today().date() #.date() extract only the date and removes the time
    mean_vol = data['volume'].mean()
    # print(mean_vol)
    def fill_blank_vol(value):
        if pd.isnull(value):
            return mean_vol
        else:
            return value
    data['volume'] = data['volume'].apply(fill_blank_vol)
    # print(data.tail(10))
    data.to_csv('transform/transformed_stock_data.csv', index = False)
    print('Data has been transformed and written to csv successfully')


# transform_data()


# Data loading layer
# Here we load in the stock_data into our postgresql after creating our database name
def load_to_dbase():
    data = pd.read_csv('transform/transformed_stock_data.csv') #Read the csv file
    engine = create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
    data.to_sql('stock_data', con = engine, if_exists= 'replace', index = False)
    print('Data successfully loaded into postgresql database')

#load_to_dbase()


#combine_data()
#transform_data()
#load_to_dbase()
  