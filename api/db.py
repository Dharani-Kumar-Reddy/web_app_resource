from flask import jsonify
from decimal import Decimal
import pymysql
from django.http import JsonResponse

def query(querystr,return_json=True):
    
    connection=pymysql.connect( host='ameerdbinstance.cryvpwsuupug.us-east-2.rds.amazonaws.com',
                                user='admin',
                                password='Ameerdb00',
                                db='prac',
                                cursorclass=pymysql.cursors.DictCursor )
    
    connection.begin()
    cursor=connection.cursor()
    cursor.execute(querystr)
    result=encode(cursor.fetchall())
    connection.commit()
    cursor.close()
    connection.close()
    if return_json:
         return JsonResponse(result,safe=False)
    else:
        return result

def encode(data):
    for row in data:
        for key,value in row.items():
            if isinstance(value,Decimal):
                row[key]=str(value)
    return data
