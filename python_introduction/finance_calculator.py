monthly_income = float (input ("Enter your monthly income "))
monthly_expenses = float (input ("Enter your monthly expenses "))
monthly_savings = float (monthly_income - monthly_expenses)
interest_rate = 0.05
number_of_months = 12
annual_savings = monthly_savings * number_of_months
example = interest_rate * number_of_months * monthly_savings

projected_savings = (float (annual_savings) + float (example))

print ( " Your monthly savings are ", (monthly_savings))
print ( "Projected savings afer one year, with interest, is: ", projected_savings)

#print (example)
#print ( annual_savings) 
