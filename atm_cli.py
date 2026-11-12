# ATM TRANSACTION SIMULATOR

from getpass import getpass
import time
import uuid


pin = '1234'

def show():
    print("\n", time.ctime())
    print("\n|__WELCOME TO SBI__|\n")
    print("\n 1> CASH WITHDRAWAL")
    print("\n 2> CHECK BALANCE")
    print("\n 3> DEPOSIT MONEY")

def verify_pin():
    available_balance = 500
    attempt = 3

    while (attempt > 0):  

        input_user1 = input("\nDo you want to withdraw? (yes/no): ").strip().lower()

        if input_user1 == 'yes':

            input_user2 = int(input("\nHow much money do you want to withdraw? "))

            if input_user2 <= available_balance and input_user2 > 0:

                _input_ = getpass("\nEnter your correct pin: ").strip()

                if _input_ == pin:
                    print("\nProcessing......")
                    time.sleep(2)

                    available_balance -= input_user2

                    print("\nACCESS GRANTED!")
                    print(f"\nYour available balance is {available_balance}")

                    input_user3 = input("\nDo you want a receipt for this transaction? ").strip().lower()

                    if input_user3 == 'yes':
                        print("\nBANK NAME            : SBI")
                        print("DATE AND TIME        :", time.ctime())
                        print("TRANSACTION STATUS   : SUCCESSFUL")
                        print("AVAILABLE BALANCE    :", available_balance)
                    else:
                        print("\nTHANK YOU FOR USING\n\n")
                    break

                else:
                    print("\nProcessing......")
                    time.sleep(2)
                    print("\nTRY AGAIN....!")
                    print("PLEASE ENTER CORRECT PIN.")
                    attempt -= 1
                    print(f"You have only {attempt} attempts left\n")
            else:
                print(f"\nEnter correct amount!")

        elif input_user1 == 'no':

            user_choice = input("\nDo you want to deposit money or check balance? (deposit/check): ").strip().lower()

            if user_choice == 'deposit':
                deposit_amount = int(input("\nEnter deposit amount: "))
                if deposit_amount > 0:
                    _input_ = getpass("\nEnter your correct pin: ").strip()
                    if _input_ == pin:
                        print("\nProcessing......")
                        time.sleep(2)

                        available_balance += deposit_amount
                        print(f"\nDeposit successful. Available balance is {available_balance}")
                        break
                    else:
                        print("\nIncorrect PIN!")
                        attempt -= 1
                else:
                    print("\nEnter valid amount to deposit.")

            elif user_choice == 'check':
                _input_ = getpass("\nEnter your correct pin: ").strip()
                if _input_ == pin:
                    print("\nProcessing......")
                    time.sleep(2)

                    print(f"\nYour available balance is: {available_balance}")
                    break
                else:
                    print("\nIncorrect PIN!")
                    attempt -= 1

            else:
                print("\nInvalid option. Try again.")

        else:
            print("\nInvalid response. Please type 'yes' or 'no'.")

    print("\n________THANK YOU_________\n\n")

def main():
    show()
    verify_pin()

main()