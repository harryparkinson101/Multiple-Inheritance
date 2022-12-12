class User(object):

  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'Attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, arrows):
    self.name = name
    self.arrows = arrows

  def check_arrows(self):
    print(f'{self.arrows} remaining')

  def run(self):
    print('Ran really fast')

  def fire(self):
    self.arrows = self.arrows - 1
    print ('you just fired, you have {self.arrows} remaining')

class Hybrid(Wizard, Archer):
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)


hybrid1 = Hybrid('Stanley', 20, 7)
archer1 = Archer('Robin', 50)
wizard1 = Wizard('Harry', 1)
#checks number of arrows
print(archer1.check_arrows())

#fires an arrow and shows remaining arrows
archer1.fire()
print(archer1.check_arrows())

# test wizard attack
print(wizard1.attack())

# test hybrid attack
print(hybrid1.attack())

# check user sign in
print(hybrid1.sign_in())

