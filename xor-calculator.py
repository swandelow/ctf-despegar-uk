
x = list("30167b0eb4eef511ec82272b4b47a2d71471")
y = list("1319057cb23c1dcbf616876372617fff8b48")

def toInt(val):
	return int(val, 16) 

values = []
for i in range(len(x)):
	# aplico XOR 
	values.append(toInt(x[i]) ^ toInt(y[i]))

# formateo los caracteres e imprimo el resultado.
result = ['{:x}'.format(i) for i in values]
print("".join(result))
