import random

games_list = []
while True:
    User_Input = input("🎮 Type add, view or edit or random game: ")
    User_Input = User_Input.strip()
    match User_Input:
        case 'add':
            game = input("🎮 Enter game name: ")
            games_list.append(game)
            print(f'🎮 Added {game} to the list 🎮')
        case 'view':
            for i in games_list:
                print(f'{i}')
        case 'random game':
            random_game = random.choice(games_list)
            print(random_game)
