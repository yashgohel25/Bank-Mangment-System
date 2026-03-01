import json
import random
import string
from pathlib import Path



class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("not Such file exist ")
    except Exception as err:
        print(f"error might be {err}")

    @classmethod 
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountnumbergenrated(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        info = {
            "name": input("Tell your name "),
            "age": int(input("Tell your age : - ")),
            "email": input("tell your email "),
            "pin": int(input("Tell your 4 digit pin :-")),
            "AccountNO." : Bank.__accountnumbergenrated(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:

            print("Sorry Your Account Does not Created any Problem age or pin ")
        else:
            print("Your Account has been Created Successful")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Note Down Your Account")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accountno = input("Tell your Account number ")
        pin = int(input("Tell your 4 digit pin "))

        userdata = [i for i in Bank.data if i['AccountNO.'] == accountno and i['pin'] == pin]
        if userdata == False:
            print("Sorry Your Account Not Found ")
        else:
            ammount = int(input("Tell the amount you want to deposit "))
            if ammount > 100000 or ammount < 0:
                print("Sorry you can not deposit this amount ")
            else:
                userdata[0]['balance'] += ammount
                print(f"Your current balance is {userdata[0]['balance']}")
                Bank.__update()

    def withdrawmoney(self):
        accountno = input("Tell your Account number ")
        pin = int(input("Tell your 4 digit pin "))

        userdata = [i for i in Bank.data if i['AccountNO.'] == accountno and i['pin'] == pin]
        if userdata == False:
            print("Sorry Your Account Not Found ")          
        else:
            ammount = int(input("Tell the amount you want to withdraw "))
            if ammount > userdata[0]['balance'] or ammount < 0:
                print("Sorry you can not withdraw this amount ")
            else:
                userdata[0]['balance'] -= ammount
                print(f"Your current balance is {userdata[0]['balance']}")
                Bank.__update()
    def accountdetails(self):
        accountno = input("Tell your Account number ")
        pin = int(input("Tell your 4 digit pin "))

        userdata = [i for i in Bank.data if i['AccountNO.'] == accountno and i['pin'] == pin]
        if userdata == False:
            print("Sorry Your Account Not Found ")          
        else:
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accountno = input("Tell your Account number ")
        pin = int(input("Tell your 4 digit pin "))

        userdata = [i for i in Bank.data if i['AccountNO.'] == accountno and i['pin'] == pin]
        if userdata == False:
            print("Sorry Your Account Not Found ")          
        else:
            print("press 1 for updating name ")
            print("press 2 for updating email ")
            print("press 3 for updating pin ")

            check = int(input("Tell your reasoned :- "))

            if check == 1:
                userdata[0]['name'] = input("Tell your new name ")
                print("Your name has been updated successfuly")
                Bank.__update()
            if check == 2:
                userdata[0]['email'] = input("Tell your new email ")
                print("Your email has been updated successfuly")
                Bank.__update()
            if check == 3:
                newpin = int(input("Tell your new 4 digit pin "))
                if len(str(newpin)) != 4:
                    print("Sorry you can not update this pin ")
                else:
                    userdata[0]['pin'] = newpin
                    print("Your pin has been updated successfuly")
                    Bank.__update()
user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposit money in the bank")
print("press 3 foe withdrawing money ")
print("press 4 for details ")
print("press 5 for updating details")
print("press 6 for delete your account ")

check = int(input("tell your reasoned :- "))

if check  == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.accountdetails()       
if check == 5:
    user.updatedetails()