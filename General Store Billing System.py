               
print("Welcome to the Python General Store!!!")

inventory = {"sugar":80 , "milk":100 , "rice":70 , "oil":120 , "eggs":15 , "salt":40 , "soap":20 , "shampoo":50 , "flour":90 , "beef":400 , "chicken":200 , "cold drink":30 , "juice":25 , "apple":10 , "banana":10 , "orange":15 , "grapes":30 , "strawberry":25 , "potatoes":10 , "onion":15 , "carrots":20 , "tomatoes":10 }
print("{:15}{}".format("Items", "Price"))
for i, j in inventory.items():
    print("{:15}Rs.{}".format(i.title(), j))
basket = []
total = []

print("\nWarning: 'Small letters are usable only!'")

def cashier ():
    user_answer = input("\nWhat do you want to purchase?: ").lower()
    while user_answer != "quit":
        if user_answer in inventory:
            basket.append(user_answer)
            user_answer = input ("Ok, I will add this to your basket! anything else?"
                                 "(Type 'quit' to end): ").lower()
        else:
            user_answer = input("I am really sorry, we don't have this item, anything else?"
                                "(Type 'quit' to end)").lower()

    
cashier()

print("\nHere are all the items in your shopping cart:")
for i in range(0,len(basket)):
    print(basket[i].title(), end=" ")


    

answer = input("\nDo you wish to buy anything esle? (Type yes/no) ")

if answer == 'yes':
    cashier()
    print("Here is all groceries you ordered: ", basket)
    for items in basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)
        
    

else:
    for items in basket:
        total.append(inventory[items])
    amount_to_pay = sum (total)
        
    
print("-----------------------------------------")
print("\nYour Items:")
for i in range(0, len(basket)):
    print("{:10}{}".format(' ',basket[i].title()))
print("-----------------------------------------")

for j in range(0, len(total)):
    print("{:10}Rs.{}".format(' ',total[j]))
    
print("-----------------------------------------")
print("Total ammount: ", amount_to_pay)
print("-----------------------------------------")

discount = 0

if amount_to_pay in range(0,101):
    discount = 0/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (0%):",discount)
    
elif amount_to_pay in range(101,201):
    discount = 1/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (1%):" , discount)

elif amount_to_pay in range(201,301):
    discount = 2/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (2%):" , discount)

elif amount_to_pay in range (301,401):
    discount = 3/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (3%):" , discount)

elif amount_to_pay in range(401,501):
    discount = 4/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (4%):" , discount)

elif amount_to_pay in range (501,601):
    discount = 5/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (5%):" , discount)

elif amount_to_pay in range (601,701):
    discount = 6/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (6%):" , discount)

elif amount_to_pay in range (701,801):
    discount = 7/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (7%):" , discount)

elif amount_to_pay in range (801,901):
    discount = 8/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (8%):" , discount)

elif amount_to_pay in range (901,1001):
    discount = 9/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (9%):" , discount)

elif amount_to_pay in range (1001,1101):
    discount = 10/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (10%):" , discount)
    
else:
    discount = 15/100*amount_to_pay
    after_discount = amount_to_pay - discount
    print("Discount (15%):" , discount)
    



print("-----------------------------------------")

print("Deduction: ", amount_to_pay , "-" , discount)
print("-----------------------------------------")
print("Net ammount: ", after_discount,"/- Rupees only")
print("-----------------------------------------")

print("\nThanks for visiting. \nWe hope you are happy with our Services \nFor any complain \nContact us: 0800-001-969 \nShop Manager: Abdul Rahim , Saad Ashraf , Shayan Nawaz , Muhammad Hammad ")
