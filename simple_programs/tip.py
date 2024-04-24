
def main():
    # prompt the user to enter a value
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # multiplis two value  total money and percentage of that money user want to tip and divides them with 100 to get the percentage value
    tip = dollars * percent /100
    # prints the tip value 
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #removed the $ from input
    d = (d.strip("$"))
    return float(d)
    

def percent_to_float(p):
    #removes the % from input
    p = (p.strip("%"))
    return float(p)

#calling main function
main()
