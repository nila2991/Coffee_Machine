money = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9

#def check(cup_water, cup_milk, cup_beans):
  #global water, milk, coffee_beans, cups
  #cups_of_water = water // 200
  #cups_of_milk = milk // 50
  #cups_of_coffee = coffee // 15
  #min_cups = min(min(cups_of_water,cups_of_milk),cups_of_coffee)
  #if count_of_cups == min_cups:
  #  print("Yes, I can make that amount of coffee")
  #elif count_of_cups < min_cups:
  #  print("Yes, I can make that amount of coffee (and even", min_cups - count_of_cups, "more than that)")
  #elif count_of_cups > min_cups:
  #  print("No, I can make only", min_cups, "cups of coffee")

def machine_state():
  print('The coffee machine has:')
  print(water, 'of water')
  print(milk, 'of milk')
  print(coffee_beans, 'of coffee beans')
  print(cups, 'of disposable cups')
  print(money, 'of money')

def espresso():
  global water, coffee_beans, money
  water -= 250
  coffee_beans -= 16
  money += 4

def latte():
  global water, coffee_beans, money, milk
  water -= 350
  milk -= 75
  coffee_beans -= 20
  money += 7

def cappuccino():
  global water, coffee_beans, money, milk
  water -= 200
  milk -= 100
  coffee_beans -= 12
  money += 6

def buy_coffee():
  global cups
  print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
  clients_coffee = input()
  cups -= 1
  if clients_coffee == '1':
    espresso()
  elif clients_coffee == '2':
    latte()
  elif clients_coffee == '3':
    cappuccino()

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

def input_inf():
  machine_state()
  print('\nWrite action (buy, fill, take):')
  action = input()
  all_action(action)
  print('')
  machine_state()

input_inf()

