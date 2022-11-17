# calculator
# Built with Seahorse v0.2.3

from seahorse.prelude import *

declare_id('Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS')

class Calculoator(Account):
	owner: Pubkey
	display: i64

@instruction
def init_calculator(owner: Signer, calculator: Empty[Calculator]):
	  calculator = calculator.init(
   	 payer = owner,
   	 seeds = ['Calculator', owner]
 	 )
 	 calculator.owner = owner.key()

@instruction
def reset_calculator(owner: Signer, calculator: Calculator):
  print(owner.key(), 'is resetting', calculator.key())


  # Verify owner
  assert owner.key() == calculator.owner, 'This is not your calculator!'


  calculator.display = 0
