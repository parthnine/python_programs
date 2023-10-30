import re
s = "This is python programming"

match = re.search('program',s)
print('Start index', match.start())
print('End index', match.end())

print(match)
 
