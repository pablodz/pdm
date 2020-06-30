import psycopg2
import random
import time

host="104.154.246.252"
database="datadb"
user="postgres"
pwd="postgres"


def make_connection():

    conn = psycopg2.connect(database=database,
                            user=user, 
                            password=pwd,
                            host=host, 
                            port="5432")
    print(conn)
    return conn                            

def execute_query(conn,t,h):

    c = conn.cursor()
    c.execute("""INSERT INTO conditions(time, location, temperature, humidity) VALUES (NOW(), 'office', {}, {});""".format(int(t),int(h)))
    conn.commit()

def generate_random_data(conn):

    for i in range(400):
        t=20+random.randint(-1, 1)
        h=45+random.randint(-1, 1)
        execute_query(conn,t,h)
        time.sleep(0.5)
        print(i,end=" , ")
    

def close_connection(conn):
    conn.close() 

if __name__ == "__main__":
    conn=make_connection()
    generate_random_data(conn)
    close_connection(conn)
