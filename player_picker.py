'''This script selects players for the Price is right game by importing a CSV from gdrive and converting it into an array, 
ultimately narrowing down to one random selection from the array. One persons name can be in the array multiple times if they satisfy additional
criteria '''

import pandas as pd
import random
import numpy as np
import pdb

import argparse

parser = argparse.ArgumentParser(description='Pick out a player')
parser.add_argument("-p", "--playerschosen", help="Comma delimited list of players already chosen")

args = parser.parse_args()
players_chosen = args.playerschosen
names_to_remove = players_chosen.split(",") if players_chosen else []

df = pd.read_csv('Names.csv') 
names = []

for col in df.columns:
	new_names = df.get(col).values
	new_names = new_names[new_names != None]
	new_names = new_names[~pd.isnull(new_names)]
	stripped_names = list(map(lambda name: name.strip(), new_names))
	names = names + list(filter(lambda name: name != "", stripped_names))

filtered_names = [name for name in names if name not in names_to_remove]
player_called = random.choice(names)
print(player_called + ", Come On Down!!!")

