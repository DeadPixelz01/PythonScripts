# Functions.
def area(x, y):
    return x * y


usr_name = input('Please enter your name: ')
usr_quality_no = int(input('Please choose your quality (1/2/3/4): '))
usr_r_width = int(input('Please enter your desired width: '))
usr_r_length = int(input('Please enter your desire length: '))
usr_trade_discount = input('Need a trade discount? (y/n): ')
usr_area = area(usr_r_width, usr_r_length)

if usr_quality_no == 1:
    usr_cost = usr_area * 100
    if usr_trade_discount == 'y':
        usr_discount = usr_cost * 0.1
    else:
        usr_discount = 0
    total_cost = usr_cost - usr_discount
    print(usr_area, usr_cost, usr_discount, total_cost)

elif usr_quality_no == 2:
    usr_cost = usr_area * 70
    if usr_trade_discount == 'y':
        usr_discount = usr_cost * 0.1
    else:
        usr_discount = 0
    total_cost = usr_cost - usr_discount
    print(usr_area, usr_cost, usr_discount, total_cost)

elif usr_quality_no == 3:
    usr_cost = usr_area * 45
    if usr_trade_discount == 'y':
        usr_discount = usr_cost * 0.1
    else:
        usr_discount = 0
    total_cost = usr_cost - usr_discount
    print(usr_area, usr_cost, usr_discount, total_cost)

elif usr_quality_no == 4:
    usr_cost = usr_area * 30
    if usr_trade_discount == 'y':
        usr_discount = usr_cost * 0.1
    else:
        usr_discount = 0
    total_cost = usr_cost - usr_discount
    print(usr_area, usr_cost, usr_discount, total_cost)
