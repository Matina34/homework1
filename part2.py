#Program to calculate the number of months needed to save for a down payment on a house in Lyon

# User inputs
annual_salary =float(input("Enter your annual salary in Lyon: "))
portion_saved=float(input("Enter the portion of salary to be saved as a decimal: "))
total_cost = float(input("Enter the cost of your dream home in Lyon:  "))
semi_annual_raise= float(input("Enter the sami annual saraly raise: "))

portion_down_payment = total_cost*0.25
current_savings=0
month=0
r =0.04


#loop that runs until the current savings are greater than or equal to the portion of the down payment
while portion_down_payment > current_savings:
    current_savings += current_savings*r/12  
    current_savings += portion_saved*(annual_salary/12)
    month +=1
    if month%6==0:
        annual_salary += annual_salary*semi_annual_raise


        

#output
print("Number of months to save for down payment:", month)



