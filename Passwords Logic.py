password = None
while password != "myPassword1234":
   password = input("Enter Something to Access This Thing: ")
   if password != "myPassword1234":
      print ("Try again")
print("Correct password. Welcome!")