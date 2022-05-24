import sys
import os
import sqlite3 as sql
from django.http import HttpResponse, request

def verFamilia(request):
    #-----------------------------------------------------------------
    current = os.getcwd()
    parent = os.path.dirname(current)
    db_location = current.replace("\\","/") + '/db.sqlite3'
    #-----------------------------------------------------------------
    # print(f'CURRENT --> {current}\nPARENT --> {parent}')
    # print(f'DB LOCATION --> {db_location}')
    #-----------------------------------------------------------------
    connection = sql.connect(db_location)
    cursor = connection.cursor()
    instruction = cursor.execute("SELECT * FROM Familia_persona")
    data = cursor.fetchall()
    #----------------------------------------------------------------
    dict_Familia = {}
    for row in data:
        dict_Familia[row[0]] = (row[1].title(), row[2].title(), row[3], row[4])

    textDocument = (str(dict_Familia))

    return HttpResponse(textDocument)