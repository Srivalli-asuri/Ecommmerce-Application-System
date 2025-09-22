🛒 StoreApp – CLI Based Shopping Application

This is a simple Python CLI application that simulates an online store.
It supports user authentication (register/login/logout) and allows users to browse products, add items to a cart, delete products, and checkout.

🚀 Features
👤 User Management

Register new users with username & password

Login with existing credentials

Logout functionality


🛍️ Product Management

View available products with prices

Add products to cart using product number

Delete products from the product list

Checkout to purchase all items in the cart

🛒 Cart Management

View items added to the cart

Calculate total price automatically

Clear cart after checkout


📂 Project Structure
StoreApp/
│── store_app.py        # Main application file (your provided code)
│── README.md           # Project documentation

⚙️ How It Works

Run the script:

python store_app.py




You’ll see the main menu:

Enter Your choice: 
1) Register  
2) Login  
3) Logout



After logging in, you’ll see the user menu:

1) View Products  
2) View Cart  
3) Checkout  
4) Delete Product  
5) Exit  



🖼️ Example Run
Enter Your choice:
1) Register  2) Login  3) Logout
choice: 1
Enter Your name: alice
Enter your Password: 1234
Registration successful

choice: 2
Enter your name: alice
Enter your password: 1234
login successful

 1) View Products
 2) View Cart
 3) Checkout
 4) Delete product
 5) Exit
Select an option: 1

Available Products:
1 .laptop - ₹ 50000
2 .earpods - ₹ 2000
3 .Watch - ₹ 1500
4 .Accessories - ₹ 1000
Enter Product Number to add: 2
earpods added to the cart for ₹ 2000

🛠️ Requirements

Python 3.6+ (recommended: Python 3.10 or above)

No external libraries required (uses only built-in Python)


💡 Future Enhancements

Add persistence (save users & products in a file or database)

Add quantity selection for products

Support discounts or offers

Add admin role for product management
