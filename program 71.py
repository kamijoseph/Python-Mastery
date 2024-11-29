
from program_70 import *

dave = BankAccount(1000, "Dave")
sara = BankAccount(1000, "Sara")
jim = InterestRewardsAcct(1000, "Jim")
blaze = SavingsAcct(1000, "Blaze")

dave.getBalance()
dave.deposit(100000)
dave.withdraw(10)
dave.transfer(10000, sara)


sara.deposit(500)
sara.getBalance()


jim.getBalance()
jim.deposit(1000)
jim.transfer(100, dave)

blaze.getBalance()
blaze.deposit(1000)
blaze.transfer(1000, sara)