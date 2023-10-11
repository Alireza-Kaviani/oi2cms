import psycopg2
from dotenv import load_dotenv
from os import environ

load_dotenv()

try:
    conn_string = f"dbname='{environ['DB_NAME']}' user='{environ['DB_USER']}' host='{environ['DB_HOST']}' password='{environ['DB_PASS']}'"
    conn = psycopg2.connect(conn_string)
except:
    print("Execution Failed: can not connect to database")
    exit()

def create_team_table(name: str):
    try:
        curs = conn.cursor()
        curs.execute(f"CREATE TABLE IF NOT EXISTS {name} (username CHAR(20) NOT NULL);")
        conn.commit()
    except:
        print(f"Failed to create '{name}' table")

    finally:
        curs.close()

def add_user_to_team(team: str, user: str):
    try:
        curs = conn.cursor()
        curs.execute(f"INSERT INTO {team} (username) VALUES('{user}');")
    except:
        print("Execution Failed")
    finally:
        conn.commit()
        curs.close()

def get_users(team: str):
    curs = conn.cursor()
    try:
        curs.execute(f"SELECT * FROM {team}")
        records = curs.fetchall()
    except:
        print("Execution Failed")
    finally:
        curs.close()

    result = []
    for record in records:
        result.append(record[0].strip())
    
    return result