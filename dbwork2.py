import pgsql
# importpip install psycopg2-binary cre2
import datetime
import json


class Database:
    _conn = 0

    def insert_data(self, data):
        """ insert multiple vendors into the vendors table  """
        self.conn = None
        try:
        #     dbn = p.parsingFile("database", True)
        #     us = p.parsingFile("user", True)
        #     pas = p.parsingFile("password", True)
        #     hos = p.parsingFile("host", True)
            try:
                db = pgsql.Connection(database="autsave", user="postgres", password="xthyjskm2000")
                db("INSERT INTO public.info(hostname, filepath, date, filesize, server) VALUES("+data[0]+","+data[1]+","+data[2]+","+data[3]+","+data[4]+")")
                db.close()


            except Exception as e: print('l09k',e)
        except Exception as e: print('ii',e)

    def insert_err(self, data):
        """ insert multiple vendors into the vendors table  """
        self.conn = None
        try:
        #     dbn = p.parsingFile("database", True)
        #     us = p.parsingFile("user", True)
        #     pas = p.parsingFile("password", True)
        #     hos = p.parsingFile("host", True)
            try:
                db = pgsql.Connection(database="autsave", user="postgres", password="xthyjskm2000")
                db("INSERT INTO public.errorlog(server, content) VALUES("+data[0]+","+data[1]+")")
                db.close()


            except Exception as e: print('l09k',e)
        except Exception as e: print('ii',e)
