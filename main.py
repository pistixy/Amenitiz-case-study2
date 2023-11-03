from cart import Cart
from product import Product
from products import products

def main():
    # Instantiate a new Cart object
    cart = Cart()
    next =""
    # Prompt the user to enter product code
    while (next!="DONE"):
        next=input("Enter one product code if you are done, enter 'DONE' (e.g., GR1,SR1,CF1): ").strip().upper()
        # Check if the provided product code exists in the available products
        if next in products:
            cart.add(products[next])
        elif next == "DONE":
            cart.display()
            print("Thanks for purchasing!")
            break
        else:
            # Notify the user if a provided product code is not recognized
            print(f"Product code {next} not recognized.")

        # Display the content of the cart, including product details and prices
        cart.display()

# Ensures the main function is executed only when this script is run directly and not imported
if __name__ == "__main__":
    main()
