import math


def ah_low_bin():
    print(" \nWrite current price on ah")

    bid = input()  # price

    while(bid.isnumeric() is False):
        print("The price is measured in numbers, try again")
        bid = input()

    bid = int(bid)

    print("Write the lowest BIN price on ah")

    lowest_bin = input()  # lowest sell bin value

    while(lowest_bin.isnumeric() is False):
        print("The bin is measured in numbers, try again")
        lowest_bin = input()

    lowest_bin = int(lowest_bin)

    print(" \nCONCLUSION \n")

    new_bid = bid * 1.1
    profit = (lowest_bin - 1) * 0.99

    if(new_bid > lowest_bin):
        print(f'No profit, cuz\nOur bin - {int(new_bid)} ; lowest Bin or market - {lowest_bin}')
        print(f'So our profit will be {int(profit - int(new_bid))}')

    else:
        if(new_bid * 1.1 < profit):
            print("smb still can bid")
            print(f'Need to make this bid - {int(math.floor(profit / 1.1))}')

        elif(new_bid > profit):
            print(f'NO PROFIT, cuz\nlowest bin - {lowest_bin}, our bid - {int(new_bid)}')
            print(f'So our profit - {int(profit - new_bid)}')

        else:
            print(f'PROFITABLE, all good. Our profit will be {int(profit - new_bid)}')

    print()


def craft_item():
    print()

    item_count = '1'  # while != we inserting new items for crafting
    total_cost = 0
    info_total_cost = ''
    possibilities = {'0', 'n', 'no', 'not', 'nah', 'noo', 'nno'}

    while item_count.lower() not in possibilities:
        print("Write the price for ONE item")

        item_price = input()  # what the price of this 1 item

        while(item_price.isnumeric() is False):
            print("The item price is measured in numbers, try again")
            item_price = input()

        item_price = int(item_price)

        print()
        print("How many of that need to use?")

        amount_of_the_item = input()  # how many we gonna use to craft

        while(amount_of_the_item.isnumeric() is False):
            print("The amount is measured in numbers, try again")
            amount_of_the_item = input()

        amount_of_the_item = int(amount_of_the_item)

        total_cost += item_price * amount_of_the_item
        info_total_cost += str(item_price) + ' * ' + str(amount_of_the_item) + ' + '
        print()
        print("Do we need to use smth else?\nWrite 1/Y/YES if u need to, or 0/N/NO")

        item_count = input()  # checking, is that all or we need to use smth else

    print()
    print("Whats the lowest price on BIN?")

    ah_bin_cost = input()  # the lowest BIN price for this item

    while(ah_bin_cost.isnumeric() is False):
        print("The bin cost is measured in numbers, try again")
        ah_bin_cost = input()

    ah_bin_cost = int(ah_bin_cost) - 1

    print()
    print("CONCLUSION")
    print()

    if(total_cost < ah_bin_cost * 0.99):
        print("PROFITABLE to craft and sell!")
    else:
        print("heres no reason to craft that, cuz")

    print(f'price of materials: {info_total_cost}= {total_cost} ; ah cost - {ah_bin_cost}')
    print(f'so profit gonna be - {int(ah_bin_cost * 0.99 - total_cost)}')


def command_table():
    print(' \nchoose the method! (write a digit) \n'
          '0 - end the programm \n'
          '1 - buy on ah and sell on bin \n'
          '2 - craft and sell on bin \n'
          '100 - look at the command table \n'
          '101 - formulas table')


def formula_table():
    print(" \nuse the same numbers from the command table, write 100 to see that")
    global formula_choose
    formula_choose = int(input())
    if(formula_choose == 1):
        print('bid + 10% bid to make a new bid \n'
              '1% tax when u selling item on ah \n'
              '-1 to make this the lowest bin \n'
              'write 1 for more details')

        more_details = int(input())

        if(more_details == 1):
            print('New bid = bid + 10% bid /or/ 1.1 * bid \n'
                  'profit = bin - 1% bin /or/ 0.99 * bin \n'
                  'bid => 1.1 * bid => (1.1 * bid) -1 => (1.1 * bid - 1) * 0.99     '
                  'P.S. -1 to make this bin the lowest')

    elif(formula_choose == 2):
        print('bid + 10% bid to make a new bid \n'
              '1% tax when u selling item on ah \n'
              '-1 to make this the lowest bin \n'
              'write 1 for more details')
        more_details = int(input())
        if(more_details == 1):
            print('total cost = (amount of items * price of this 1 item) also how many types of item /n'
                  'current lowest bin - 1 => to make out the lowest \n'
                  '1 % tax from selling so (bin - 1) - 1% bin /or/ (bin - 1) * 0.99')
    elif(formula_choose == 100):
        command_table()
        formula_table()
    else:
        print("didnt find any method, try again")
        formula_table()


command_table()
choose_the_method = int(input())

'''
def method(choose_the_method):
    switcher = {
        1: ah_low_bin(),
        2: craft_item(),
        100: command_table()
    }
    return switcher.get(choose_the_method, "didnt found any method, try again")
'''

while choose_the_method > 0:

    if(choose_the_method == 1):
        ah_low_bin()
    elif(choose_the_method == 2):
        command_table()
    elif(choose_the_method == 100):
        command_table()
    elif(choose_the_method == 101):
        formula_table()
    else:
        print("didnt found any method, try again")

    if(choose_the_method != 100):
        print(" \nif u done, just write 0, or 100 to see command table")

    choose_the_method = int(input())
