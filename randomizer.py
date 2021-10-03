import json
import random

randList = []
for i in range(1000):
	randList.append(i+1)
random.shuffle(randList)

for i in range(1000):
	with open("jsons/" + str(i)) as f:
		data = json.load(f)

	with open("jsonsNew/" + str(randList[i]), 'w') as f:
		json.dump(data, f, indent=2)
