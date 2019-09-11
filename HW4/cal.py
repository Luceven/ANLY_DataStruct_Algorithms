res = []
with open("results.txt", "r") as file:
	for line in file:
		for word in line.split():
			res.append(float(word))

#print(res[0:10])

print("Average Runtime:", sum(res)/len(res))