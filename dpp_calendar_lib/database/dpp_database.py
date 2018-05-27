import sqlite3
from datetime import datetime, timedelta

database = "dpp_calendardb.db"
def select_all():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    events = cursor.execute("SELECT * FROM Event")
    #connection.close()
    return list(events)

def input(date, name, description, frequency, amount):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    for i in range(0, amount):
        print("Inserting ", i)
        cursor.execute("INSERT INTO Event(Id, Name, Description, Date) VALUES (NULL, ?, ?, ?)",
        (name, description, date))
        if frequency == "None":
            pass
        elif frequency == "Day":
            delta = timedelta(days=1)
        elif frequency == "Week":
            delta = timedelta(weeks=1)
        elif frequency == "Month":
            delta = timedelta(days=30)
        date = date + delta
    connection.commit()
    connection.close()
    return

def remove(id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Event WHERE Id = (?)", id)
    connection.commit()
    connection.close()

def populate_database():    
    date = datetime.now()    
    name = "Event name"
    description = "Event description"
    frequency = "Week"
    amount = 10
    insert(date, name, description, frequency, amount)
    return