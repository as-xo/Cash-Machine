def main():
# function to ask for customer account number
   def verify_account():
      try: 
         account_number = int(input("Enter your Account Number: "))
         if account_number != len(6):
            raise ValueError ("Invalid account number format. Please enter a 6-digit account number")
      finally:
         print("Account Number accepted.")
      return verify_account()
       

# function asking for PIN verification
   def verify_pin():
      try:
         pin_number = int(input("Enter your PIN Number: "))
         if pin_number != len(4):
            
            raise ValueError ("Invalid PIN format. Please enter a numeric value.")
      finally:
         print("PIN number accepted!")   
# func for transaction options


# func for withdrawal handling


# finally block to display "Thank you for using the ATM"

if __name__ == "_main__":
   main()