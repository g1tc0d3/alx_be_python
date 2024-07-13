
def safe_divide (numerator, denominator):

    try:
        if numerator or denominator == 0:
            raise ZeroDivisionError ("Division by Zero not allowed")
    except:
        ValueError
        print("Error! please enter numeric values only")

        return numerator/denominator