'''This script selects players for the Price is right game by importing a CSV from gdrive and converting it into an array, 
ultimately narrowing down to one random selection from the array. One persons name can be in the array multiple times if they satisfy additional
criteria '''

import pandas as pd
import random
import numpy as np
import pdb

# import argparse

# parser = argparse.ArgumentParser(description='Pick out a player')
# parser.add_argument("-p", "--playerschosen", help="Comma delimited list of players already chosen")

# args = parser.parse_args()
# players_chosen = args.playerschosen
# names_to_remove = players_chosen.split(",") if players_chosen else []

names_to_remove = []

def reloadNames():
	names = []
	df = pd.read_csv('Names.csv')
	for col in df.columns:
		new_names = df.get(col).values
		new_names = new_names[new_names != None]
		new_names = new_names[~pd.isnull(new_names)]
		stripped_names = list(map(lambda name: name.strip(), new_names))
		names = names + list(filter(lambda name: name != "", stripped_names))
	return names

names = reloadNames()

while (True):
	command = input("Enter command. reload for reloading CSV, choose to pick player\n")
	if command == "reload":
		names = reloadNames()
	elif command == "choose":
		filtered_names = [name for name in names if name not in names_to_remove]
		if filtered_names == []:
			print("No players left to choose")
		else:
			player_called = random.choice(filtered_names)
			print("Come on down " + player_called)
			names_to_remove.append(player_called)
	elif command == "exit":
		exit()
	else:
		print("command not recognized")
