import pandas as pd
from sqlalchemy import create_engine

# 1. Put your actual details here
FILE_PATH = "C:\\Users\\rajen\\Downloads\\IPL_Ball_by_Ball_2008_2022.csv"
USER = "root"
PASSWORD = "1234"
HOST = "localhost"
DATABASE = "campusx"
TABLE_NAME = "ipl"

# 2. Read the file
df = pd.read_csv(FILE_PATH)

# 3. Connect to MySQL
connection_string = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
engine = create_engine(connection_string)

# 4. Send data to MySQL
df.to_sql(name=TABLE_NAME, con=engine, if_exists='replace', index=False)

print("Success! Data uploaded.")
