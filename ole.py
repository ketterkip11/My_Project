import json

# Opening JSON file
import pandas as pd

f = open('api_data.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

df = pd.DataFrame.from_dict(data, orient='columns')
# print(df.head())

from sqlalchemy import create_engine
import psycopg2

# INPUT YOUR OWN CONNECTION STRING HERE
conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )


# perform to_sql test and print result
db = create_engine(conn)
# conn = db.connect()


df.to_sql('api20', con=conn, if_exists='replace', index=False)

