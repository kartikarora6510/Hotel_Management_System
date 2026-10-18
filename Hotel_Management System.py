import pickle
import random
import os
print("*****WELCOME TO Taj blue HOTEL*****\n")
list=[]
list1=[]
list2=[]
while True:
    print("1.Enter Customer Data")
    print("2.Calculate Room Rent")
    print("3.Calculate Restaurant Bill")
    print("4.Calculate Laundry Bill")
    print("5.Calculate Game Bill")
    print("6.Show Total Cost")
    print("7.Previous Customer Deatils:")
    print("8.EXIT\n")
    ch=int(input("Choose Any option:"))
    if(ch==1):
        cust=input("Enter Ur name:")
        address=input("Enter Ur Address:")
        checkin=input("Enter check-In Date:")
        checkout=input("Enter check-Out Date:")
        customer_D = {
        "Name": cust,
        "Address": address,
        "Checkin": checkin,
        "Checkout": checkout,
        }
        k=random.randrange(95,777)
        print("You Room Number is:",k)
    elif(ch==2):
        print("We have the following rooms for you:-")
        print()
        print(r"1.type A---->rs 6000 PN\-")
        print(r"2.type B---->rs 5000 PN\-")
        print(r"3.type C---->rs 4000 PN\-")
        print(r"4.type D---->rs 3000 PN\-")
        print()
        room=int(input("Choose Any option:"))
        how=int(input("How Many Night Do you stay:"))
        if(room==1):
            c=6000*how
            print(c)
        elif(room==2):
            c=5000*how
            print(c)
        elif(room==3):
            c=4000*how
            print(c)
        elif(room==4):
            c=3000*how
            print(c)
        else:
            print("Invalid Input")
    elif(ch==3):
        print("*****RESTAURANT MENU*****","\n")
        print(r"1.breakfast combo--->Rs500")
        print(r"2.lunch---->Rs800")
        print(r"3.Dinner--->Rs1500")
        print(r"4.Liquor--->Rs5000")
        print(r"5.Exit","\n")
        while True:
            oops=int(input("Enter You Choose:"))
            if(oops==5):
                print("Total Food Cost:",sum(list))
                break
            count=int(input("Enter the quantity:"))
            if(oops==1):
                d=500*count
                list.append(d)
            elif(oops==2):
                d=800*count
                list.append(d)
            elif(oops==3):
                d=1500*count
                list.append(d)
            elif(oops==4):
                d=5000*count
                list.append(d)
            else:
                print("Invalid Output")
    elif(ch==4):
        print("******LAUNDRY MENU*******","\n")
        print(r"1.Shorts----->Rs30")
        print(r"2.Trousers----->Rs40")
        print(r"3.Shirt--->Rs50")
        print(r"4.Jeans---->Rs60")
        print(r"5.Girlsuit--->Rs80")
        print(r"6.Exit","\n")
        while True:
            gullu=int(input("Enter You Choose:"))
            if(gullu==6):
                print("Total Laundry Cost:",sum(list1))
                break
            jullu=int(input("Enter the Cloths quantity:"))
            if(gullu==1):
                j=30*jullu
                list1.append(j)
            elif(gullu==2):
                j=40*jullu
                list1.append(j)
            elif(gullu==3):
                j=50*jullu
                list1.append(j)
            elif(gullu==4):
                j=60*jullu
                list1.append(j)
            elif(gullu==5):
                j=80*jullu
                list1.append(j)
            else:
                print("Invalid Output")
    elif(ch==5):
        print("******GAME MENU*******","\n")
        print(r"1.Table tennis----->Rs250")
        print(r"2.Bowling----->Rs200")
        print(r"3.Snooker--->Rs350")
        print(r"4.Video games---->Rs400")
        print(r"5.Pool--->Rs500")
        print(r"6.Exit","\n")
        while True:
            o=int(input("Enter You Choose:"))
            if(o==6):
                print("Total Game Cost:",sum(list2))
                break
            w=int(input("No. of Hours:"))
            if(o==1):
                w=250*w
                list2.append(w)
            elif(o==2):
                w=200*w
                list2.append(w)
            elif(o==3):
                w=350*w
                list2.append(w)
            elif(o==4):
                w=400*w
                list2.append(w)
            elif(o==5):
                w=500*w
                list2.append(w)
    elif(ch==6):
        print("******HOTEL BILL*******","\n")
        print(r"Customer details:")
        print(r"Customer name:",cust)
        print(r"Customer address:",address)
        print(r"Check in date:",checkin)
        print(r"Check out date:",checkout)
        print(r"Room no:",k)
        print("Your Room rent is:",c)
        print("Your Food bill is:",sum(list))
        print("Your laundary bill is:",sum(list1))
        print("Your Game bill is:",sum(list2))
        final=(c+sum(list)+sum(list1)+sum(list2))
        print("Your Sub total bill is:",final)
        print("Additional Service Charges is 18%(Rs1800)")
        print("Your grandtotal bill is:",final+1800)
        obj=open("Details.dat","ab")
        customer = {
        "Name": cust,
        "Address": address,
        "Checkin": checkin,
        "Checkout": checkout,
        "Room_no": k,
        "Room_rent": c,
        "Food_bill": sum(list),
        "Laundry_bill": sum(list1),
        "Game_bill": sum(list2),
        "Subtotal": final,
        "Service_charge": 1800,
        "Grand_total": final + 1800
        }
        pickle.dump(customer,obj)
        obj.close()
    elif(ch==7):
        print("****** All CUSTOMER DETAILS ******\n")
        print("1.Search by Customer Name:")
        print("2.Search by Checkin date:")
        print("3.Search by Room Number:")
        
        try:
            gug=int(input("Choose Any one option:"))
        except Exception:
            print("Please enter a valid number")
            continue
        if not os.path.exists("Details.dat"):
            print("No previous customer records found.")
            continue
        if(gug==1):
            ent=input("Enter Customer name:")
        elif(gug==2):
            kar=input("Enter Checkin date")
        elif(gug==3):
            rag=int(input("Enter Room Number"))
        found=False
        
        with open("Details.dat","rb")as obj:
            while True:
                try:
                    customer=pickle.load(obj)
        
                    if gug == 1:
                        if (customer["Name"].lower().strip()==ent.lower().strip()):
                            found=True
                            
                    
                    if gug == 2:
                        if(customer["Checkin"].lower().strip()==kar.lower().strip()):
                            found=True
                    
                    if gug == 3:
                        if(customer["Room_no"]==rag):
                            found=True
                    if found:
                        print("\n****** CUSTOMER FOUND ******")
                        print("Customer Name:", customer["Name"])
                        print("Customer Address:", customer["Address"])
                        print("Check in Date:", customer["Checkin"])
                        print("Check out Date:", customer["Checkout"])
                        print("Room No:", customer["Room_no"])
                        print("Room Rent:", customer["Room_rent"])
                        print("Food Bill:", customer["Food_bill"])
                        print("Laundry Bill:", customer["Laundry_bill"])
                        print("Game Bill:", customer["Game_bill"])
                        print("Subtotal:", customer["Subtotal"])
                        print("Service Charge:", customer["Service_charge"])
                        print("Grand Total:", customer["Grand_total"])
                except EOFError:
                    break
        if(found==False):
            print("Customer Not Found")
    elif(ch==8):
        print("Thanks for Visiting Taj Hotel")
        quit()
                
      
        
            
                
                
                
        
        
        
                    
        
        
        
            
        


    
        
        
    
    
