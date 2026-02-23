def get_params(x0,y0,x1,y1):
	if x1 != x0:
		alpha = (y1-y0)/(x1-x0)
		beta = y0 - alpha*x0
	else:
		alpha = 0
		beta = 0
	return alpha,beta

def get_output(x,alpha,beta):
	return alpha*x + beta

def interpolate(values, init = 0.0, end = 20.0, step=0.01):
	x_f = []

	v0 = init

	while v0 <= end:
		x_f.append(v0)
		v0 += step
		v0 = round(v0,10)
	x_i = []
	y_i = []
	i_lower = 0
	for x in x_f:
		i_upper = len(values)-1
		for i in range(i_lower, len(values)):
			if x > values[i][0]:
				i_lower = i
			elif x < values[i][0]:
				i_upper = i
				break
			else:
				i_upper = i
				i_lower = i_upper
				break

		if (i_lower == i_upper and x >= values[0][0] and x <= values[len(values)-1][0]):
			x_i.append(x)
			y_i.append(values[i_upper][1])
		elif (i_lower == i_upper):
			x_i.append(x)
			y_i.append(0)
		else:
			a,b = get_params(values[i_lower][0],values[i_lower][1],values[i_upper][0],values[i_upper][1])
			y = get_output(x,a,b)
			x_i.append(x)
			y_i.append(y)
	return x_i, y_i





