# Packages
import sqlite3
from dotenv import load_dotenv
from rich import print as rprint
import json
import os
import requests
import random

load_dotenv()

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
    User_Input = input("🎮 Type add, view or remove or edit or random game or if you have a steam account you can use Steam: ")
    User_Input = User_Input.strip()
    match User_Input:
        case 'add':
            game = str(input("🎮 Enter game name: "))
            c.execute(' INSERT INTO Games (GameName,GameRating,GameDescription) VALUES (?,"To be added","To be added")',(game,))
            conn.commit()
            rprint(f'🎮 Added {game} to the list 🎮')
        case 'view':
            games = c.execute('SELECT Gamename,GameDescription, GameRating FROM Games')
            for games in c:
                rprint(f'name: {games[0]}\n'
                      f'Description: {games[1]}\n'
                      f'Rating: {games[2]}\n')
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
                rprint(f'name: {games[0]}\n'
                      f'Description: {games[1]}\n'
                      f'Rating: {games[2]}\n')
        case 'Steam':
            steam_key = os.getenv("STEAMAPIKEY")
            your_steam_id = os.getenv("YOUR_STEAM_ID")
            Steam_api_owned_games = requests.get(f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steam_key}&steamid={your_steam_id}&include_appinfo=True&format=json')
            Steam_api_json = Steam_api_owned_games.json()
            game_name = []
            games_appid = []
            for game_appid in Steam_api_json['response']['games']:
                games_appids = game_appid['appid']
                games_appid.append(games_appids)
            random_game = random.choice(games_appid)
            Steam_store_api_url = f'https://store.steampowered.com/api/appdetails?appids={random_game}'
            Steam_store_api_response = requests.get(Steam_store_api_url)
            Steam_store_api_json = Steam_store_api_response.json()
            Steam_store_picture = Steam_store_api_json[str(random_game)]['data']['header_image']
            Steam_store_short_description = Steam_store_api_json[str(random_game)]['data']['short_description']
            params = {
                "key": steam_key,
                "steamid": your_steam_id,
                "format": "json",
                "include_appinfo": "true",
                "appids_filter[0]": random_game,
            }
            url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
            Steam_api_owned_games_appid = requests.get(url, params=params)
            steam_owned_games_appid_json = Steam_api_owned_games_appid.json()
            for game in steam_owned_games_appid_json['response']['games']:
                game_names = game['name']
                games_playtime = game['playtime_forever'] / 60
            rprint(f"link to an image of the game: {Steam_store_picture}")
            rprint(f'Game Name: {game_names}')
            rprint(f'description of the game: {Steam_store_short_description})')
            rprint(f'Time played:{games_playtime:.2f} hours')
