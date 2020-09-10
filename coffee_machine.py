money = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9

def machine_state():
  print('The coffee machine has:')
  print(water, 'of water')
  print(milk, 'of milk')
  print(coffee_beans, 'of coffee beans')
  print(cups, 'of disposable cups')
  print('${}'.format(money), 'of money')

def check(name, resource, cup_need):
  if cup_need > resource:
    return name + ', '
  else:
    return '+'

def make_coffee(water_cup, milk_cup, beans_cup, money_cup):
  global water, milk, coffee_beans, cups, money
  water -= water_cup
  milk -= milk_cup
  coffee_beans -= beans_cup
  cups -= 1
  money += money_cup


def espresso():
  global water, coffee_beans, cups, money
  enough = check('water', water, 250) + check('coffee beans', coffee_beans, 16) + check('disposable cups', cups, 1)
  if enough == '+++':
    make_coffee(250, 0, 16, 4)
    print('I have enough resources, making you a coffee!')
  else:
    print('Sorry, not enough {}!'.format(enough.strip(' ,+')))


def latte():
  global water, milk, coffee_beans, cups, money
  enough = check('water', water, 350) + check('milk', milk, 75) + check('coffee beans', coffee_beans, 20) + check('disposable cups', cups, 1)
  if enough == '++++':
    make_coffee(350, 75, 20, 7)
    print('I have enough resources, making you a coffee!')
  else:
    print('Sorry, not enough {}!'.format(enough.strip(' ,+')))

def cappuccino():
  global water, milk, coffee_beans, cups, money
  enough = check('water', water, 200) + check('milk', milk, 100) + check('coffee beans', coffee_beans, 12) + check('disposable cups', cups, 1)
  if enough == '++++':
    make_coffee(200, 100, 12, 6)
    print('I have enough resources, making you a coffee!')
  else:
    print('Sorry, not enough {}!'.format(enough.strip(' ,+')))

def buy_coffee():
  print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
  clients_coffee = input()
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
  water += int(input())
  print('Write how many ml of milk do you want to add:')
  milk += int(input())
  print('Write how many grams of coffee beans do you want to add:')
  coffee_beans += int(input())
  print('Write how many disposable cups of coffee do you want to add:')
  cups += int(input())

def take_money():
  global money
  print('I gave you ${}'.format(money))
  money = 0

def all_action(action):
  if action == 'buy':
    buy_coffee()
  elif action == 'fill':
    fill_machine()
  elif action == 'take':
    take_money()
  elif action == 'remaining':
    machine_state()
  elif action == 'exit':
    return 0
  print()

def input_inf():
  print('Write action (buy, fill, take, remaining, exit):')
  action = input()
  print()
  return all_action(action)

while input_inf() != 0:
  continue

