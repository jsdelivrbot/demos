import anydbm

db = anydbm.open('websites','c')

#Add an item.
db['www.python.org'] = 'Python home page'

print db['www.python.org']

# Close and save to dist.
db.close()
