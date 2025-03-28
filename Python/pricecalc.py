def calculate_discount(price,discount_percentage):
    
    userinput = input("Enter originalprice and the discount given using the format(10000,20)")

    price,discount_percentage = userinput.split(",")

    price,discount_percentage = int(price),int(discount_percentage)

    if discount_percentage >= 20:
        discount = price * 0.02
        new_price = price - discount
        print(f"You have been give a discount of {discount}")
        print(f"Your new paying price is {new_price}")

    else:
        print(f"Your paying price is {price}")

calculate_discount(3000,10)