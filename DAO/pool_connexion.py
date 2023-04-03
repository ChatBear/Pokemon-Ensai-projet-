import json

with open('Installation/serveur.json') as json_file:
    data = json.load(json_file)


import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import pool

class PoolConnection():



    __instance = None

    @staticmethod
    def getInstance():
        if PoolConnection.__instance is None:
            PoolConnection()
        return PoolConnection.__instance


    @staticmethod
    def getConnexion():
        return PoolConnection.getInstance().getconn()

    @staticmethod
    def closeConnexions():
        try :
            PoolConnection.getInstance().closeall
            closed = True
        except Exception :
            print("Problème lors de la fermeture")
            closed = False
        return closed

    @staticmethod
    def putBackConnexion(connection):
        PoolConnection.getInstance().putconn(connection)

    def __init__(self):

        if PoolConnection.__instance is not None:
            raise Exception("Cette classe est un singleton. Utiliser la "
                            "méthode getInstance()")
        else:
            PoolConnection.__instance = psycopg2.pool.SimpleConnectionPool(1, 10,
                                                                           host=data['host'],
                                                                          port=data['port'],
                                                                           database=data['database'],
                                                                           user=data['user'],
                                                                           password=data['password'],
                                                                           )