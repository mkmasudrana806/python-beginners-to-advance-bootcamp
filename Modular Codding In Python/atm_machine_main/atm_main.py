# ------------- ATM Machine class -------------
class AtmMachine:
  # constructor function. all the data property need to write inside constructor
  # self define it is AtmMachine class
  def __init__(self) -> None:
    self.pin = ""
    self.balance = 0
    self.menu()

  # menu method of this class
  def menu(self):
    user_input = input("""
    Hello, How would you like to proceed?
    1. Enter 1 to create pin
    2. Enter 2 to deposit
    3. Enter 3 to withdraw
    4. Enter 4 to check balance
    5. Enter 5 to change pin
    """)
    if user_input == "1":
      # create a pin
      self.create_pin()

    elif user_input == "2":
      # deposit
      self.deposit()

    elif user_input == "3":
      # withdraw
      self.withdraw()

    elif user_input == "4":
      # check balance
      self.check_balance()

    elif user_input == "5":
      # change pin
      self.change_pin()

    else:
      print("Invalid input")

  # create pin method
  def create_pin(self):
    self.pin = input("Enter your pin: ")
    print("Pin set successfully")

    self.balance = int(input("Enter your balance: "))
    print("Balance set successfully")

    print("Pin created successfully")
    self.menu()


  # change pin method
  def change_pin(self):
    old_pin = input("Enter old pin: ")

    if old_pin == self.pin:
      new_pin = input("Enter new pin: ")
      self.pin = new_pin
      print("Pin changed successfully")
    else:
      print("Invalid pin")
    self.menu()



  # deposit method
  def deposit(self):
    user_pin = input("Enter pin: ")
    if user_pin == self.pin:
      amount = int(input("Enter amount: "))
      self.balance = self.balance + amount
      print("Deposit successfully")
    else:
      print("Invalid pin")
    self.menu()


  # withdraw method
  def withdraw(self):
    user_pin = input("Enter your pin: ")
    if user_pin == self.pin:
      amount = int(input("Enter amount: "))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print("Withdraw successfully")
      else:
        print("Insufficient balance")
    else:
      print("Invalid pin")
    self.menu()


  # check balance method
  def check_balance(self):
    user_pin = input("Enter your pin: ")
    if user_pin == self.pin:
      print("Your balance is: ", self.balance)
    else:
      print("Invalid pin")
    self.menu()


