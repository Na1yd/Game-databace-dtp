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
        print(f"name                                             Game_name  Rating  Release_date  Genre")
        for game in results:
            print(f"{game[0]:<30}{game[1]:<8}{game[2]:<6}{game[3]:<6}{game[4]:<6}{game[5]:<6}")
        print(results) 


print_all_games()