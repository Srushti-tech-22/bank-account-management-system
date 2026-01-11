import random
class Account:
    def __init__(self,name=None,email=None,phone=None,address=None,account_type=None,balance=None,IFSC_CODE=None,bank_name=None,account_number=None):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address
        self.account_type=account_type
        self.balance=balance
        self.IFSC_CODE=IFSC_CODE
        self.bank_name=bank_name
        self.account_number=None

class Operations:
    def generate_account_number(self,IFSC_CODE,bank_name):
       return IFSC_CODE+bank_name+str(random.randint(10000,99999))
    def create_account(self):
        account_obj=Account(
        input("Enter the name: "),
        input("Enter the email: "),        
        input("Enter the phone: "),     
        input("Enter the address: "),     
        input("Enter the account_type 1.saving 2.Current: "),     
        float(input("Enter the balance: ")),   
        input("Enter the IFSC Code: "),   
        input("Enter the bank name: ")
    )
        account_obj.account_number=self.generate_account_number(account_obj.IFSC_CODE,account_obj.bank_name)
        print("Your account number is: ",account_obj.account_number)
        account_db.append(account_obj)
        print("Account created Successfullly....")

    def view_account(self):
            for data in account_db:
                print(data.account_number)
                print(data.account_type)
                print(data.balance)
                print(data.name)
                print(data.IFSC_CODE)
                print(data.phone)
                print(data.email)
                print(data.address)

    def delete_account(self):
        acc_no=input("Enter acc number: ")
        for data in account_db:
            if acc_no==data.account_number:
                account_db.remove(data)
                print("Account deleted successfully")
                return
        print("Acount not found")
    def update_account(self):
        acc_no=input("Enter acc number: ")
        for acc in account_db:
            if acc_no == acc.account_number:
                print("1.update name")
                print("2.update email")
                print("3.update phone")
                print("4.update address")

                choice=int(input("Choose the field to update: "))
                if choice==1:
                    acc.name=input("Enter new name: ")
                elif choice==2:
                    acc.email=input("Enter new email")
                elif choice==3:
                    acc.phone=input("Enter new phone no.")
                elif choice==4:
                    acc.address=input("Enter new address")
                else:
                    print("Invalid choice")
                
                print("Updated Successfully")
                return

        print("Account not found")

    def count_total_account(self):
        print("Total account: ",len(account_db))
    def search_account_by_number(self):
        acc_no=input("Enter the acc number: ")
        for acc in account_db:
            if acc_no==acc.account_number:
                print("name: ",acc.name)
                print("emial: ",acc.email)
                print("phone: ",acc.phone)
                print("balance: ",acc.balance)
                return
        print("Account not found")
    def deposit_amount(self):
        acc_no=input("Enter the acc number: ")
        for acc in account_db:
            if acc_no==acc.account_number:
                amount=int(input("Enter amount to deposite: "))
                acc.balance+=amount
                print("Amount deposited successfully")
                return
    def debit_amount(self):
        acc_no = input("Enter the acc number: ")
        for acc in account_db:
            if acc_no == acc.account_number:
                amount = int(input("Enter amount to debit: "))
                if amount > acc.balance:
                    print("Insufficient balance")
                acc.balance -= amount
            print("Amount debited successfully")
        print("Account not found")
    def view_balance(self):
        acc_no=input("Enter the acc number: ")
        for acc in account_db:
              if acc_no == acc.account_number:
                 print("Balance: ", acc.balance)
                 return
        print("Account not found")

   

if __name__ == '__main__':
    account=Account()
    account_db=[]
    operations=Operations()
    while True:
       print("1. add account\n"
             "2. view account\n"
             "3.count Total Account\n"
             "4. Delete Account\n"
             "5. Update Account\n"
             "6. Search Account\n"
             "7. deposit Account\n"
             "8.debit amount\n"
             "9.view balance\n"
             "10.Exit")
       choice=int(input("Please choose once...."))
       if choice==1:
           operations.create_account()
       elif choice==2:
            operations.view_account()
       elif choice==3:
            operations.count_total_account()
       elif choice==4:
        operations.delete_account()
       elif choice==5:
            operations.update_account()
       elif choice==6:
            operations.search_account_by_number()
       elif choice==7:
            operations.deposit_amount() 
       elif choice==8:
            operations.debit_amount()   
       elif choice==9:
            operations.view_balance()
       elif choice == 10:
            print("Thank you for using the system")
            break

        
        

