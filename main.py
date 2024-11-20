# Packages
import sqlite3

while True:
    #connect to DB -> If DB does not exist this will create the db
    conn = sqlite3.connect('game.db')
    #Creates cursor
    c = conn.cursor()
    #creates table if it does not exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS Games(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        GameName TEXT NOT NULL,
        GameRating TEXT,
        GameDescription TEXT 
        )'''
        )
    #Saves created table
    conn.commit()
    print(f'This has been created to track the games I have been playing along with picking a random game to play')
    User_Input = input("🎮 Type add, view or remove or edit or random game: ")
    User_Input = User_Input.strip()
    match User_Input:
        case 'add':
            game = str(input("🎮 Enter game name: "))
            c.execute(' INSERT INTO Games (GameName,GameRating,GameDescription) VALUES (?,"To be added","To be added")',(game,))
            conn.commit()
            print(f'🎮 Added {game} to the list 🎮')
        case 'view':
            games = c.execute('SELECT Gamename,GameDescription, GameRating FROM Games')
            for games in c:
                print(f'name:{games[0]}\n'
                      f'Description:{games[1]}\n'
                      f'Rating:{games[2]}\n')
        case 'remove':
            RemovedGamesName = str(input("🎮 Enter game name: "))
            c.execute('DELETE FROM Games WHERE GameName = ?',(RemovedGamesName,))
            conn.commit()
        case 'edit':
            choice = str(input("Please type if you want to change the name,description or rating of the game: "))
            match choice:
                case 'name':
                    NameOfGame = str(input("🎮 Enter game name you want to change: "))
                    NewGameName = str(input("🎮 Enter the name of the game: "))
                    c.execute('UPDATE Games SET GameName = ? WHERE GameName = ?',(NewGameName,NameOfGame))
                    conn.commit()
                case 'description':
                    NameOfGame = str(input("🎮 Enter game name you want to change: "))
                    Description = str(input("🎮 What is the Description of the game: "))
                    c.execute('UPDATE Games SET GameDescription = ? WHERE GameName = ?', (Description, NameOfGame))
                    conn.commit()
                case 'rating':
                    NameOfGame = str(input("🎮 Enter game name you want to change: "))
                    Rating = str(input("🎮 What is the Rating of the game out of 5: "))
                    c.execute('UPDATE Games SET GameRating = ? WHERE GameName = ?', (Rating, NameOfGame))
                    conn.commit()
        case 'random game':
            c.execute('SELECT Gamename,GameDescription, GameRating FROM Games ORDER BY RANDOM() LIMIT 1')
            for games in c:
                print(f'name:{games[0]}\n'
                      f'Description:{games[1]}\n'
                      f'Rating:{games[2]}\n')
