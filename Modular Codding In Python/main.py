from atm_machine_main.atm_main import AtmMachine as Atm
from atm_machine_main.db import Database

print('ok')

# all the import is done here
db = Database()
atm = Atm()

# this is a common pattern that, all the import methods or anything is written below
if __name__ == '__main__':
    db.database_connection()
    atm.create_pin()
    atm.check_balance()