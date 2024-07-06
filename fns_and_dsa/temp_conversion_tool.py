def FAHRENHEIT_TO_CELSIUS_FACTOR():
    factor = float(5/9)
    # print (5/9)
    return()
def CELSIUS_TO_FAHRENHEIT_FACTOR():
    # print (9/5)
    return()
def convert_to_celsius ():
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    fahrenheit = float(input("Enter the temparature to convert: "))
    unit = input("Is this temparature in Celsius or Fareinheit? (C/F): ")
    match unit:
        case "F":
            conversion = ((fahrenheit - 32) / FAHRENHEIT_TO_CELSIUS_FACTOR)
        case "C":
            print("Temparature in Celsius")
        
convert_to_celsius()
CELSIUS_TO_FAHRENHEIT_FACTOR()
FAHRENHEIT_TO_CELSIUS_FACTOR()

    
           
FAHRENHEIT_TO_CELSIUS_FACTOR()
CELSIUS_TO_FAHRENHEIT_FACTOR()
