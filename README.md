This Python program simulates a simple pharmacy transaction where a user can select products to purchase, and the program generates a receipt with the selected items and their prices. 
The program begins by greeting the user and displaying an inventory list from a file called "inventory.txt." 
The user is then prompted to choose from various products like masks, hand sanitizer, Clorox wipes, hand soap, and gloves, with the prices stored in a dictionary. 
The user can choose up to three products.

After the product selection, the program asks if the user wants a receipt and, if so, what type of card they are using. 
It then opens a graphical user interface (GUI) window using the Tkinter library, displaying the store name, receipt details, and card type. 
The receipt lists each purchased item with its price, calculates the subtotal, and adds tax to display the total cost. 
Finally, a "Print Receipt" button is available, and clicking it displays the final receipt with all the details.
