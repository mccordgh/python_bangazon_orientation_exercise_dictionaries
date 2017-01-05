my_family = { 'mother' : { 'name': 'Nancy', 'age': 60 },  'father' : { 'name': 'Jim', 'age': 66 }, 'brother' : { 'name': 'Adam', 'age': 30 }, 'sister' : { 'name': 'Elisabeth', 'age': 37 }, 'me' : { 'name': 'Matthew', 'age': 33 } }

for (relationship, info) in my_family.items():	
	print('{0} is my {1} and is {2} years old'.format(info['name'], relationship, info['age']))