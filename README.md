# Game Picker

## Description

I have created this to keep track of games I am playing or I am currently playing, I have the overall logic worked out I am going make an alternate version in the future so that I can selfhost a website to check or view my games.

## Steam intergration

Steam is a massive platform and having a list for your games is good but it can take a bit of time so instead I have added steam intergration, this will do the following:

It will randomly pick a game:
   - It will show the name of the game
   - It will show a header image of the game
   - It will show the time you have already played
   - It will give you a description of the game from the store page.

### How to create your steam api key :

https://steamcommunity.com/dev and click the "Go to Registration page" text at the bottom of the page.

### How to find your steam ID:
On the steam application and at the top right of the app click your profile and click account details.

Your steam ID is under the "your Account" text at the top of the page

You will need to create an .env file and add the following enviroment variables:
```
STEAMAPIKEY = <ADD YOUR STEAM KEY HERE>

YOUR_STEAM_ID = <ADD YOUR STEAM ID HERE>
```

## To do list

- Make to more random options, I think if a game is finished there could be a replay option if you are currently playing there could be an option for that and if you have not started it yet then you can pick that.

- More fields for the table for the above point.

- more options for edit for the above point.

## Set up

Clone the repo

```
git clone https://github.com/scottieyarn1135/game-picker.git
```
Going into the repo and installing required packages
```
cd game-picker

pip install -r requirements.txt

touch .env

add the following to the .env file:

STEAMAPIKEY = <ADD YOUR STEAM KEY HERE>

YOUR_STEAM_ID = <ADD YOUR STEAM ID HERE>
```
Starting the application
```
python3 main.py
```
