medical_cause=input("Did you have a medical cause to skip school Y or N: ")
attendance=int(input("Enter your attendance this year: "))
if medical_cause=="Y":
 print("Allowed")
else:
 if attendance>=75:
  print("Allowed")
 else:
  print("not allowed")