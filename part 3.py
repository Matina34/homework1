# Bisection search to find best savings rate


total_cost = 1000000 
portion_down_payment = total_cost*0.25 

annual_return = 0.04
semi_annual_raise = 0.07
tolerance = 100


# Function to simulate savings for 36 months
def saving_guess (annual_salary,portion_saved):
    T = 36
    current_savings = 0

    
    for n in range (1,T+1):

        # Add monthly savings
        current_savings += portion_saved* annual_salary/12

        # Add monthly investment return
        current_savings += current_savings * annual_return/12 
        

         # Apply semi-annual raise
        if n%6==0:
            annual_salary *= (1 + semi_annual_raise)

    return current_savings

if __name__ == '__main__':

    annual_salary =float(input("Enter the starting salary in Lyon: "))


    low1=0
    high1=1
    bisection_steps=0
    

    # First check if the whole annual salary would be enough or not:
    max_portion = (saving_guess(annual_salary,high1))

    if portion_down_payment > max_portion :
        print("It is not possible to pay the down payment in three years.")


    else :
        
        
        
        while True :
            

            bisection_steps += 1

            guess = (low1+high1)/2
            save = saving_guess(annual_salary, guess)
            
            
            if abs(portion_down_payment - save) <= 100 :
                best_portion = guess
                break
                
            elif save > portion_down_payment:
                    high1 = guess
                    

            else :
                    low1 = guess

            
            
                     
        print (f"Best savings rate:{best_portion:.4f}")
        print(f"Steps in bisection search:{bisection_steps}")
       