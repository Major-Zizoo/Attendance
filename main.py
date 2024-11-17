Medical=input("Enter you have taken medical leave Y or N:")
Attend= int(input("Enter attendance days."))

if Medical=="Y":
    print("Allowed")
else:
    if Attend>=75:
     print("Allowed")
    else:
       print("Not Allowed")