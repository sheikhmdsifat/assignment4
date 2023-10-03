def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
        
        if hours <= 40:
            pay = hours * rate
        else:
            regular_pay = 40 * rate
            overtime_pay = (hours - 40) * (rate * 1.5)
            pay = regular_pay + overtime_pay
        
        return pay
    except ValueError:
        return "Error, please enter numeric input"

try:
    hours = input("Enter the number of hours worked: ")
    rate = input("Enter the hourly rate: ")
    
    salary = computepay(hours, rate)
    
    if isinstance(salary, float):
        print(f"Salary: ${salary:.2f}")
    else:
        print(salary)
except KeyboardInterrupt:
    print("Program terminated by user.")
