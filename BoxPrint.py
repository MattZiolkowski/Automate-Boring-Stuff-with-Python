#! python3
# Program prints out the "boxes" out of symbols- the real purpose is to introduce user to usage of try and exeption mode.

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')

    print(symbol*width)
    for i in range(height-2):
        print(symbol+(' '*(width-2))+symbol)
    print(symbol*width)



for sym, w, h in (('$', 5, 5),('P', 50, 10), ('3',1,10)):
    try:
        boxPrint(sym, w, h)
    except Exception as error:
        print('An exception happened: '+ str(error))
