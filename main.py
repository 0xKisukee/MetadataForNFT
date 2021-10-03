import json
import ast
import random

def idGen(num):
	if num < 10:
		string = "\"#000" + str(num) + "\""
		return string
	elif num < 100:
		string = "\"#00" + str(num) + "\""
		return string
	elif num < 1000:
		string = "\"#0" + str(num) + "\""
		return string
	elif num < 10000:
		string = "\"#" + str(num) + "\""
		return string

metadata = []

with open("all-traits.json") as f:
	data = json.load(f)

i=0
for element in data:

	metadata.append("{" + 	"\"" + "description" + "\"" + ":" + "\"" + "DESCRIPTION" + "\"" + "," + 
						"\"" + "external_url" + "\"" + ":" + "\"" + "WEBSITE" + "\"" + "," + 
						"\"" + "image" + "\"" + ":" + "\"" + "ipfs://IPFS/" + str(element["tokenId"]) + ".jpg" + "\"" + "," + 
						"\"" + "name" + "\"" + ":" + idGen(element["tokenId"]) + "," + 
						"\"" + "attributes" + "\"" + ":" + "[")

	metadata.append(	"{" + "\"" + "trait_type" + "\"" + ":" + "\"" + "Background" + "\"" + "," + "\"" + "value" + "\"" + ":" + "\"" + element["Background"] + "\"" + "}" + "," + 
					"{" + "\"" + "trait_type" + "\"" + ":" + "\"" + "Can" + "\"" + "," + "\"" + "value" + "\"" + ":" + "\"" + element["Can"] + "\"" + "}" + "]" + "}")

	final = "".join(metadata)
	final = ast.literal_eval(final)
	with open("jsons/" + str(i), 'w') as f:
		json.dump(final, f, indent=2)
	metadata = []
	i = i + 1
