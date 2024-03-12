'''
Banking System with Menu 
'''
# import modules
import sqlite3
import bcrypt
import random

# create a class Banking
class Banking:
    #create a constructor
    def __init__(self,db_name="banking.db"):
        # open the connection to the db file
        self.con = sqlite3.Connection(db_name)
        # create a cursor
        self.cursor = self.con.cursor()
        self.create_tables()

     # create table
    def create_tables(self):
        # execute SQL statement
        self.cursor.execute('''
CREATE TABLE IF NOT EXISTS branches(
        id INTEGER PRIMARY KEY,
        branch_name TEXT,
        branch_location TEXT
        )
''')
        self.cursor.execute('''
CREATE TABLE IF NOT EXISTS customers(
    cust_id INTEGER PRIMARY KEY,
    cust_name TEXT,
    cust_password TEXT,
    cust_acc_num INTEGER,
    cust_branch_id INTEGER,
    FOREIGN KEY (cust_branch_id) REFERENCEs branches(id)
    )
''')
        self.cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts(
        acc_num INTEGER PRIMARY KEY,
        balance REAL,
        credit_limit REAL
)
''')
    # execute statements
        self.con.commit()

        

    # create a branch
    def branch(self, name , location):
        # insert data
        self.cursor.execute('INSERT INTO branches (branch_name, branch_location) VALUES(?, ?)', (name , location))
        self.con.commit()
        return self.cursor.fetchall

    # create customer
    def customer(self , name , password , branch_id):
        # encrypt password
        encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # create random number between 100000 - 999999 for an account number
        acc_num = random.randint(100000, 999999 )
        self.cursor.execute('INSERT INTO customers(name , password , acc_num , branch_id) VALUES(? ,? ,?,?)',(name ,encrypted_password,acc_num , branch_id))

        self.cursor.execute('INSERT INTO accounts(acc_num, balance , credit_limit) VALUES(?, 0 ,0)',(acc_num))
        self.con.commit()
        print(self.cursor.fetchall())

    
    # create login
    def login(self, acc_num , password):
        self.cursor.excute('SELECT id , password FROM customers WHERE acc_num=?',(acc_num))
        # fetch the first row
        response = self.cursor.fetchone()
        if response and bcrypt.checkpw(password.encode('utf-8'),response[1]):
            return response[0]
        else:
            return None
    
    # apply for credit
    def credit_application(self , cus_id , amount):
        acc_num = self.get_acc_num(cus_id)
        self.cursor.execute('SELECT balance , credit_limit FROM accounts WHERE acc_num=?',(acc_num))
        balance , credit_limit =self.cursor.fetchone()
        if amount <= credit_limit:
            self.cursor.excute('UPDATE accounts SET balance=? WHERE acc_num=?',(balance + amount, acc_num))
            self.con.commit()
            return f"Credit applied successfully.New balance:{balance + amount}"
        else:
            return "Insufficient credit limit"
        
    # withdraw
        
    # deposit
        
    # get balance
    
    # get account number
    def get_acc_num(self , cus_id):
        self.cursor.execute('SELECT acc_num FROM customers WHERE id =?',(cus_id))
        return self.cursor.fetchone()[0]

# Menu
def menu():
    print("Create a Branch")
    print("Create a customer")
    print("Login")
    print("Apply for Credit Cart")

def create_branch(bank_system):
    branch_name = input("Enter branch name")
    branch_location = input("Enter branch location")
    bank_system.branch(branch_name , branch_location)
    print("created")

if __name__ == "__main__":
    bank = Banking()
    while True:
        menu()
        choice = input("Enter your choice(0-6)")
        if choice == "1":
            create_branch(bank)
