
# while month < 12:
#     month += 1
#     portion_saved 





# portion_down_pmt = 0.25

# # DWN (.25) - Total COST

# salary divided by 12
# monthly income div by 12
# variable = current savings
# creat a counter
# 

# break into months
# create variable monthly salary
# everything in months
# every loop equals a month



# while month > 1:
#     print (current_savings * .10)
#     month = month -1

total_cost = float(input ("What is the total cost of your dream home?"))
annual_salary = float(input ("What is your starting annual salary?"))
portion_saved = float(input ("What is your portion to be saved?"))

r = .04
current_savings = 0
down_pmt = (.25 * total_cost)
monthly_salary = (annual_salary / 12) * (portion_saved)
monthly_return = (r/12)
month = 0


while current_savings < (down_pmt):
    month += 1
    current_savings += (monthly_return * current_savings) + monthly_salary

    # print (month)
    print ("Number of months is" , month)

   



