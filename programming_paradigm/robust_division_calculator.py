
def safe_divide (numerator, denominator):
    print (numerator/denominator)
    if numerator or denominator == 0:
        raise ZeroDivisionError ("Division by Zero not allowed")

    return numerator/denominator