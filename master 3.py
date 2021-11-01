"""Arya Bhanushali
1st Period
Master Project
4/23/2020"""

from tkinter import *



def main():
    print("Welcome to the Pharmacy!")
    file = ("Inventory")
    print(file)
    f = open("inventory.txt", "r")
    print(f.read())
    #reads the text file called inventory and prints products and prices written

    mask_pack = 8.50
    hand_sanitizer = 5.00
    clorox = 6.25
    hand_soap = 4.50
    gloves = 15

    choice_prices = {}
    #dictionary that organizes product with it's price

    choice1 = input("What are you buying today? ")
    if (choice1 == "mask pack" or choice1=="Masks" or choice1=="masks"):
        choice_prices['Mask Pack of 50'] = mask_pack
    if (choice1 == "hand sanitizer" or choice1=="Hand Sanitizer"):
        choice_prices['16oz Hand Sanitizer'] = hand_sanitizer
    if (choice1 == "clorox" or choice1=="Clorox" or choice1=="wipes"):
        choice_prices['Clorox Disinfecting Wipes'] = clorox
    if (choice1 == "hand soap" or choice1=="Hand Soap"):
        choice_prices['16 oz Hand Soap'] = hand_soap
    if (choice1 == "gloves" or choice1=="Gloves"):
        choice_prices['100PC Disposable Latex Gloves'] = gloves
        #add products to the dictionary based on input choice

    again = input("Would you like anything else? ")
    if (again.lower() == "yes"):
        choice2 = input("What else would you like? ")
        if (choice2 == "mask pack" or choice2=="Masks" or choice2=="masks"):
            choice_prices['Mask Pack of 50'] = mask_pack
        if (choice2 == "hand sanitizer" or choice2=="Hand Sanitizer"):
            choice_prices['16oz Hand Sanitizer'] = hand_sanitizer
        if (choice2 == "clorox" or choice2=="Clorox" or choice2=="wipes"):
            choice_prices['Clorox Disinfecting Wipes'] = clorox
        if (choice2 == "hand soap" or choice2=="Hand Soap"):
            choice_prices['16 oz Hand Soap'] = hand_soap
        if (choice2 == "gloves" or choice2=="Gloves"):
            choice_prices['100PC Disposable Latex Gloves'] = gloves
        again2 = input("Would you like anything else? ")

        if (again2 == "Yes" or again2 == "yes"):
            choice3 = input("What else would you like? ")
            if (choice3 == "mask pack" or choice3=="Masks" or choice2=="masks"):
                choice_prices['mask Pack of 50'] = mask_pack
            if (choice3 == "hand sanitizer" or choice3=="Hand Sanitizer"):
                choice_prices['16oz Hand Sanitizer'] = hand_sanitizer
            if (choice3 == "clorox" or choice3=="Clorox" or choice3=="wipes"):
                choice_prices['Clorox Disinfecting Wipes'] = clorox
            if (choice3 == "hand soap" or choice3=="Hand Soap"):
                choice_prices['16 oz Hand Soap'] = hand_soap
            if (choice3 == "gloves" or choice3=="Gloves"):
                choice_prices['100PC Disposable Latex Gloves'] = gloves
            intro()
        else:
            intro()

    else:
        intro()
    window = Tk()
    window.title("Receipt")
    window.geometry("350x350")
    title = Label(window, text="ABC Pharmacy", font=("Courier", 30))
    title.pack()
    lbl = Label(window, text="Reciept", font=("Arial Bold", 20))
    lbl.pack()
    card=Label(window, text="{} Credit #:*************".format(cardtype))
    card.pack()
    btn = Button(window, text="Print Receipt", fg="red", command=lambda: clicked(choice_prices, title, lbl, card, window))
    btn.pack()
    window.mainloop()
    #creats the window where the receipt will be printed, button uses a lambda function


def intro(cardtype):
   
    intro = input("Would you like a receipt? ")
    if (intro.lower() == "yes"):
        cardtype = input("Select one: Discover, Visa, Mastercard ")
        verify_card = input("You will be paying with a {}? ".format(cardtype))


def clicked(choice_prices, title, lbl, card, window):
    total=0
    alist=[]
    time = (date_time.date_now())
    lbl.configure(text=time, font=(18))
    #replaces former text with the text written in a seperate time module
    if (len(choice_prices) == 1):
        for key, value in choice_prices.items():
            ch1 = Label(window,text= "1 {}: ${}".format(key, value), font=("Arial Bold", 12))
            ch1.pack()
            total+=value
            alist.append(value)
        #the built in function len( ) allows the list values to be appended based on the number of inputs
        #formats the product and corresponding price on the GUI
            
    if (len(choice_prices) == 2):
        total = 0
        for key, value in choice_prices.items():
            ch1 = Label(window, text="1 {}: ${}".format(key, value),font=("Arial Bold", 12))
            ch1.pack()
            total+=value
            alist.append(value)
            
    if (len(choice_prices) == 3):
        total = 0
        for key, value in choice_prices.items():
            ch1 = Label(window, text="1 {}: ${}".format(key, value),font=("Arial Bold", 12))
            ch1.pack()
            total+=value
            alist.append(value)
    labelsubtotal=Label(window, text="Subtotal: ")
    labelsubtotal.pack()
    subtotal=Label(window, text=sum(alist))
    #adds all values in the list and is labeled as subtotal
    subtotal.pack()
    withtax=Label(window, text="Total with tax: ", font=("Arial Bold", 10))
    withtax.pack()
    tax=Label(window, text=sum(alist)*.08+sum(alist), font=("Arial Bold", 10))
    #calculates total by adding tax
    tax.pack()
    


if (__name__ == "__main__"):
    main()







