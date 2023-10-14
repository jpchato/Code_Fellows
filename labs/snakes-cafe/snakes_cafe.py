def main():
    print_menu()
    orders = {}
    
    while True:
        user_input = input("> ").strip()
        
        if user_input.lower() == 'quit':
            print("Thank you for visiting Snakes Cafe. Goodbye!")
            break
        
        if user_input in orders:
            orders[user_input] += 1
        else:
            orders[user_input] = 1
        
        print(f"** {orders[user_input]} orders of {user_input} have been added to your meal **")
        

def print_menu():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
    """)


if __name__ == "__main__":
    main()
