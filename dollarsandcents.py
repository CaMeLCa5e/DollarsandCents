#dollars and cents

def convert_units (val, name):
	result = str(val)+ " "+ name
	if val > 1:
		result = result + "s"
	return result
	
def convert (val):
	dollars = int(val)
	cents = int(round(100 * (val - dollars)))
	
	#convert to strings
	dollars_string = convert_units (dollars, "dollar")
	cents_string = convert_units(cents, "cent")
	
	#return composite string
	if dollars == 1 and cents == 0:
		return "Broke!"
	elif dollars == 0:
		return cents_string
	elif cents == 0:
		return dollars_string
	else:
		return dollars_string + " and " + cents_string
		
		
    
# Tests
print convert(11.23)
print convert(11.20) 
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)