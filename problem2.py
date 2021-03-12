budget=int(input("Enter your budget : "))
productDict={}
while True:
  print("1. Add Item")
  print("2. Show list")
  print("3. Exit")
  choice=input("Enter Your Choice : ")
  if choice=="1":
    productName=input("Enter Product : ")
    productQuantity=input("Enter Quantity : ")
    productPrice=input("Enter Price : ")
    if productPrice.isnumeric():
      print("Price should be numeric !")
    if not productQuantity.isalpha():
      print("Quantity should be Alphanumeric !")
    productPrice=int(productPrice)
    if productPrice>budget:
      print("You do not have Enough budget!")
      print("Your budget : ",budget)
      continue
    elif budget==0:
      print("You have 0 budget!")
    elif(productName in productDict.keys()):
      productDict[productName][0]=productDict[productName][0]+" + "+productQuantity
      productDict[productName][1]=productDict[productName][1]+productPrice
      print("Product Quantity Increased")
    else: 
      productDict[productName]=[productQuantity,productPrice]
      print(productDict[productName])
      print("Product Added to the List.")
    budget-=productPrice
  if choice=="2":
    print("Products -> ")
    for i in productDict.items():
      print("Name:",i[0],"Quantity:",i[1][0],"Price:",i[1][0])      
  if choice=="3":
    break
  print("These items Can be brought in the remaining budget...")
  for i in productDict.items():
    if(i[1][1]<=budget):
      print("Name:",i[0],"Quantity:",i[1][0],"Price:",i[1][0])