money = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9

class Coffee_Machine():
  state = 'None'

  def decision(self, choice):
    if self.state == 'Start':
      return all_action(choice)
    if self.state == 'buy_coffee':
      buy_coffee(choice)
    if self.state == 'fill_machine':
      return choice


def check(name, resource, cup_need):
  if cup_need > resource:
    return name + ', '
  else:
    return '+'


def machine_state():
  print('The coffee machine has:')
  print(water, 'of water')
  print(milk, 'of milk')
  print(coffee_beans, 'of coffee beans')
  print(cups, 'of disposable cups')
  print('${}'.format(money), 'of money')

def espresso():
  global water, coffee_beans, cups, money
  enough = check('water', water, 250) + check('coffee beans', coffee_beans, 16) + check('disposable cups', cups, 1)
  if enough == '+++':
    print('I have enough resources, making you a coffee!')
    water -= 250
    coffee_beans -= 16
    cups -= 1
    money += 4
  else:
    print('Sorry, not enough {}!'.format(enough.strip(' ,+')))


def latte():
  global water, milk, coffee_beans, cups, money
  enough = check('water', water, 350) + check('milk', milk, 75) + check('coffee beans', coffee_beans, 20) + check('disposable cups', cups, 1)
  if enough == '++++':
    print('I have enough resources, making you a coffee!')
    water -= 350
    milk -= 75
    coffee_beans -= 20
    cups -= 1
    money += 7
  else:
    print('Sorry, not enough {}!'.format(enough.strip(' ,+')))

def cappuccino():
  global water, milk, coffee_beans, cups, money
  enough = check('water', water, 200) + check('milk', milk, 100) + check('coffee beans', coffee_beans, 12) + check('disposable cups', cups, 1)
  if enough == '++++':
    print('I have enough resources, making you a coffee!')
    water -= 200
    milk -= 100
    coffee_beans -= 12
    cups -= 1
    money += 6
  else:
    print('Sorry, not enough {}!'.format(enough.strip(' ,+')))

def buy_coffee(clients_coffee):
  if clients_coffee == '1':
    espresso()
  elif clients_coffee == '2':
    latte()
  elif clients_coffee == '3':
    cappuccino()
  elif clients_coffee == 'back':
    input_inf()

def fill_machine():
  global water, milk, coffee_beans, cups
  print('Write how many ml of water do you want to add:')
  water += new_client.decision(int(input()))
  print('Write how many ml of milk do you want to add:')
  milk += new_client.decision(int(input()))
  print('Write how many grams of coffee beans do you want to add:')
  coffee_beans += new_client.decision(int(input()))
  print('Write how many disposable cups of coffee do you want to add:')
  cups += new_client.decision(int(input()))

def take_money():
  global money
  print('I gave you ${}'.format(money))
  money = 0

def all_action(action):
  print()
  if action == 'buy':
    new_client.state = 'buy_coffee'
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    new_client.decision(input())
  elif action == 'fill':
    new_client.state = 'fill_machine'
    fill_machine()
  elif action == 'take':
    take_money()
  elif action == 'remaining':
    machine_state()
  elif action == 'exit':
    return 0
  print()

def input_inf():
  new_client.state = 'Start'
  print('Write action (buy, fill, take, remaining, exit):')
  return new_client.decision(input())

new_client = Coffee_Machine()

while input_inf() != 0:
  continue
