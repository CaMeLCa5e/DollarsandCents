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
		
#define draw handler
def draw(canvas):
	canvas.draw_text (convert(value), [60,110], 24, "white")
		
#def an input field handler
def input_handler(text):
	global value
	value = float(text)
	
	
#create frame
frame = simplegui.create_frame("Converter", 400, 200)

#register event handlers
frame.set_draw_handler(draw)
frame.add_input("Enter value", input_handler, 100)

# start frame
frame.start()


# Tests
print convert(11.23)
print convert(11.20) 
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)