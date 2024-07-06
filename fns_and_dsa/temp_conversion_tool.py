FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
    
def convert_to_celsius ():
    fahrenheit = float(input("Enter the temparature to convert: "))
    unit = input("Is this temparature in Celsius or Fareinheit? (C/F): ")
    match unit:
        case "F":
            conversion = ((fahrenheit - 32) / FAHRENHEIT_TO_CELSIUS_FACTOR)
            print (f"{fahrenheit} is {conversion}")
        case "C":
            print("Temparature in Celsius")
        
convert_to_celsius()

