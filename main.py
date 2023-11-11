# Importing necessary classes from other modules
from cart import Cart
from products import products

def main():
    # Create an instance of Cart, which will hold the selected products
    cart = Cart()
    
    # Initialize a variable to control the while loop for product input
    next = ""
    
    # Continue prompting the user for input until they type 'DONE'
    while (next != "DONE"):
        # Ask the user for a product code or to enter 'DONE' to finish shopping
        next = input("Enter one product code or type 'DONE' to complete your purchase (e.g., GR1,SR1,CF1): ").strip().upper()
        
        # Check if the input is a product code that exists in our products list
        if next in products:
            # Add the corresponding product to the cart
            cart.add(products[next])
        elif next == "DONE":
            # The user has finished adding products, display the final cart contents
            cart.display()
            # Thank the user for their purchases and exit the while loop
            print("Thanks for purchasing!")
            break
        else:
            # The input was not a valid product code, inform the user
            print(f"Product code '{next}' not recognized.")
        
        # Display the current contents of the cart after each product is added
        cart.display()

# This condition checks if the script is being run directly (as opposed to being imported)
# This is good practice for making Python scripts executable as programs
if __name__ == "__main__":
    main()
