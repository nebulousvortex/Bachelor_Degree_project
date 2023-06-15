import pymysql
import pandas as pd
import pyodbc
import sys
import random
from random import randint
import datetime

if __name__=="__main__":
    print("USE [Heat Electric Central]")
    print("GO")
    print()
    #'''
    
    startDateTime = datetime.datetime(2022,12,12,00,00,00)
    timeInterval = datetime.timedelta(seconds=10)
    for i in range(200):
        temperature = randint(80, 110)
        pressureIndex = random.uniform(0.5, 1.2)
        idealPressIndex = 0.7
        query = "INSERT INTO [dbo].[Boiler_Room]([Time],[Temperature],[Pressure],[IdealPress])"+ '\n' + \
                "VALUES ('" + str(startDateTime) + "', " + str(round(temperature, 2)) +", " + \
                str( round( pressureIndex * temperature , 2)) +", " + str(round(idealPressIndex * temperature , 2))+ ")"
        print(query)
        startDateTime += timeInterval
