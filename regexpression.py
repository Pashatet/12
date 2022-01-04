import re
# mytext = 'awdawd@mail.ru, pasha - 1999: Olesya 1999, pavel-5529@mai..ru, Ross Vega, Bobby Hudson, Kaliyah Clements, Jairo Robinson ,Victor Vega'


# textlookfor = r'\w{6}\s'

# textlookfor = r'[A-Z][a-z]+'
# allresults = re.findall(textlookfor, mytext)
# print(allresults)

input_file = 'tests/garbage_data.txt'
results_file = 'tests/results.txt'

inputfile = open(input_file, mode='r', encoding='latin-1')
resultsfile = open(results_file, mode='a', encoding='latin-1')

lookfore = r'[\w.-_]+@(?!google\.org)[\w]+\.[\w]+'
mytext = inputfile.read()

results = re.findall(lookfore, mytext)

for item in results:
    print(item)
    resultsfile.write(item + '\n')
print(len(results))
