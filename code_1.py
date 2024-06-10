'''Dylan wiliiams game database application'''

import sqlite3


DATABASE = "database.db"

#function
def print_all_games():
    '''print all the games nicely'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * from Game;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"name"                                                                                               )
        for game in results:
            print(game)
        print(results) 


print_all_games()