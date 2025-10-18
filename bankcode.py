import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",password="root123",database="banking_system")
def openacount():
    print("*************OPEN NEW ACCOUNT*************")
    accno =int(input("Enter Account No. --- "))
    name=input("Enter Name --- ")
    dob=input("Enter Date of Birth --- ")
    address=input("Enter Address --- ")
    mobno =int(input("Enter Mobile No. --- "))
    balance=int(input("Enter Opening Balance --- "))
    q1="insert into account values('{}','{}','{}','{}','{}','{}')".format(accno, name, dob, address, mobno, balance)
    q2="insert into amount values('{}','{}','{}')".format(accno, name, balance)
    c=con.cursor()
    c.execute(q1)
    c.execute(q2)
    con.commit()
    print("Congratulaions Account Opened Successfully")   
def deposit():
    print("**************DEPOSIT AMOUNT**************")
    amount=int(input("Enter Amount --- "))
    accno=input("Enter Account No --- ")
    q1="select TotalBalance from amount where Acc_no={}".format(accno)
    c=con.cursor()
    c.execute(q1)
    myresult=c.fetchone()
    b=myresult[0]
    tamount=b+amount
    q2="update amount set TotalBalance={} where Acc_no={}".format(tamount,accno)
    c.execute(q2)
    con.commit()    
def withdraw():
    print("**************WITHDRAW AMOUNT**************")
    amount=int(input("Enter Withdraw Amount ---"))
    accno=input("Enter Account No ---")
    q1="select TotalBalance from amount where Acc_no={}".format(accno)
    c=con.cursor()
    c.execute(q1)
    myresult=c.fetchone()
    b=myresult[0]
    tamount=b-amount
    q2="update amount set TotalBalance={} where Acc_no={}".format(tamount,accno)
    c.execute(q2)
    con.commit()   
def balance():
    print("**************BALANCE ENQUIRY**************")
    accno=input("\tEnter Account No ---")
    q1="select TotalBalance from amount where Acc_no={}".format(accno)
    c=con.cursor()
    c.execute(q1)
    myresult=c.fetchone()
    print("******************BALANCE*******************")
    print("\tCurrent Balance is RS",myresult[0])
def details():
    print("***********CHECK ACCOUNT DETAILS************")
    accno=input("\tEnter Account No --- ")
    q1="select * from amount where Acc_no={}".format(accno)
    c=con.cursor()
    c.execute(q1)
    myresult=c.fetchone()
    print("******************DETAILS*******************")
    for i in myresult:
        print(i,end="\t|\t")
def closeaccount():
    accno=input("\tEnter Account No --- ")
    q1="delete from account where Acc_no={}".format(accno)
    q2="delete from amount where Acc_no={}".format(accno)
    c=con.cursor()
    c.execute(q1)
    c.execute(q2)
    con.commit()
    print("\n......Account Deleted Successfully........\n")
while True:
    print("""\n
*********************************************
----------------[Bank Services]--------------
*********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
            7.Exit
*********************************************
---------------------------------------------
*********************************************
    \n""")
    choice=input("Enter Your Choice----- ")
    if(choice=='1'):
        openacount()
    elif(choice=='2'):
        deposit()
    elif(choice=='3'):
        withdraw()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        details()
    elif(choice=='6'):
        closeaccount()
    elif(choice=='7'):
        print("\n......Thank You For Choosing Our Bank Services........\n")
        break
    else:
        print("........Invalid Choice........")