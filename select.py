#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 
Course work: 
@author:
Source:
    
'''
import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'root'
database = 'postgres'

def start():
    """
    Query all rows in the CITY table
    :param conn: the Connection object
    :return:
    """    
    conn = psycopg2.connect( host = hostname, user = username, password = password, dbname = database )
    
    rows = None
    try:
        cur = conn.cursor()

        cur.execute( "SELECT * FROM ONE" )
        
        rows = cur.fetchall()
    
    except Error as e:
        print(e)
    
    
    for row in rows :
        print(row)        

        
if __name__ == '__main__':
    start()  