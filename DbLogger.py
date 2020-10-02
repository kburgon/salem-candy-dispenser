import sqlite3
import os.path

def log_trigger():
    initialize = not(os.path.exists("log.db"))
    if initialize:
        print('Table not yet initialized!')
        create_table()
    print('Inserting log into table...')
    connection = sqlite3.connect("log.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO trigger_log (loggedAt) VALUES (DATETIME('now'))")
    cursor.close()
    connection.commit()
    connection.close()
    print('Log inserted.')

def create_table():
    print('Creating table...')
    connection = sqlite3.connect("log.db")
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE trigger_log (id INTEGER PRIMARY KEY, loggedAt TEXT)')
    print('Table created.')
    cursor.close()
    connection.close()

def get_logs():
    print('Getting all entries')
    connection = sqlite3.connect("log.db")
    cursor = connection.cursor()
    cursor.execute('SELECT loggedAt FROM trigger_log;')
    table = cursor.fetchall()
    print('Results: ')
    for r in table:
        print('  ' + r[0])
    cursor.close()
    connection.commit()
    connection.close()