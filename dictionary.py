mark={'Player1':60,
'Player2':50,
'Player3':25,
'Player4':10,
'Player5':35,
}
#print(mark.values()) "prints the values only"
#print(mark.keys())    "prints the keys only"
#print(mark.items())  "prints both key-value pair
element=mark.pop('Player5',35)
print(mark)
