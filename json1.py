import json

filename = 'tests/user_settings.txt'
myfile = open(filename, mode='w', encoding='latin-1')

player1 = {
    'PlayerName': 'pasha',
    'Score': 333,
    'Awards': ['OR', 'NV', 'YES']
}

player2 = {
    'PlayerName': 'sasha',
    'Score': 300,
    'Awards': ['BY', 'TX', 'HTTPS']
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# --------save by JSON--------------

json.dump(myplayers, myfile)
myfile.close()

#-------LOAD by json----------

myfile = open(filename, mode='r')
json_date = json.load(myfile)
for person in json_date:
    print('PlayerNAME IS: ', str(person['PlayerName']))
    print('PlayerNAME IS: ', str(person['Score']))
    print('PlayerNAME IS: ', str(person['Awards'][0]))
    print('PlayerNAME IS: ', str(person['Awards'][1]))
    print('PlayerNAME IS: ', str(person['Awards'][2]))
    print('---------------')