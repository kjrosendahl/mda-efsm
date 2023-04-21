from vm import vm1, vm2 

print('Which VM machine would you like?')
print('1: VM1')
print('2: VM2')
type_vm = int(input()) 

if type_vm == 1: 
    vm1 = vm1() 

    print('Vending Machine 1') 

    print('Menu: ') 
    print('0: create(int)')
    print('1: coin(float)')
    print('2: sugar()')
    print('3: tea()')
    print('4: latte() ')
    print('5: insert_cups(int)')
    print('6: set_price(float)')
    print('7: cancel()')
    print('q: quit program')

    print('Remember these operations!')

    print('Vending Machine 1 Execution:')

    ch = '1'

    while ch != 'q': 
        print('Select Operation:')
        print('0-create, 1-coin, 2-sugar, 3-tea, 4-latte, 5-insert_cups, 6-set_price, 7-cancel, q-quit')
        ch = input()[0]

        if ch == '0': 
            print('Operation: create(int p)')
            print('Enter value of parameter p:')
            p = eval(input()) 
            vm1.create(p)
        elif ch == '1': 
            print('Operation: coin(float v)') 
            print('Enter value of parameter v:')
            v = eval(input())
            vm1.coin(v)
        elif ch == '2': 
            print('Operation: sugar()')
            vm1.sugar() 
        elif ch == '3': 
            print('Operation: tea()')
            vm1.tea() 
        elif ch == '4': 
            print('Operation: latte()')
            vm1.latte() 
        elif ch == '5': 
            print('Operation: insert_cups(int n)')
            print('Enter value of parameter n:')
            n = eval(input())
            vm1.insert_cups(n)
        elif ch == '6': 
            print('Operation: set_price(float p)')
            print('Enter value of parameter p:')
            p = eval(input())
            vm1.set_price(p)
        elif ch == '7': 
            print('Operation: cancel()')
            vm1.cancel() 

    print('Goodbye!')

elif type_vm == 2: 
    
    vm2 = vm2() 

    print('Vending Machine 2')

    print('Menu:') 
    print('0: CREATE(float)')
    print('1: COIN(int)')
    print('2: CARD(int)')
    print('3: SUGAR()')
    print('4: CREAM()')
    print('5: COFFEE()')
    print('6: InsertCups(int)')
    print('7: SetPrice(float)')
    print('8: CANCEL()')
    print('q: quit program')

    print('Remember these operations!')

    print('Vending Machine 2 Execution:')

    ch = '1'

    while ch != 'q': 
        print('Select Operation:')
        print('0-CREATE, 1-COIN, 2-CARD, 3-SUGAR, 4-CREAM, 5-COFFEE, 6-InsertCups, 7-SetPrice, 8-CANCEL, q-quit')
        ch = input()[0]

        if ch == '0': 
            print('Operation: CREATE(float p)')
            print('Enter value of parameter p:')
            p = eval(input()) 
            vm2.CREATE(p)
        elif ch == '1': 
            print('Operation: COIN(int v)') 
            print('Enter value of parameter v: ')
            v = eval(input())
            vm2.COIN(v)
        elif ch == '2': 
            print('Operation: CARD(int x)')
            print('Enter value of parameter x: ')
            x = eval(input())
            vm2.CARD(x)
        elif ch == '3': 
            print('Operation: SUGAR()')
            vm2.SUGAR() 
        elif ch == '4': 
            print('Operation: CREAM()')
            vm2.CREAM() 
        elif ch == '5': 
            print('Operation: COFFEE()')
            vm2.COFFEE() 
        elif ch == '6': 
            print('Operation: InsertCups(int n)')
            print('Enter value of parameter n: ')
            n = eval(input())
            vm2.InsertCups(n)
        elif ch == '7': 
            print('Operation: SetPrice(float p)')
            print('Enter value of parameter p: ')
            p = eval(input())
            vm2.SetPrice(p)
        elif ch == '8': 
            print('Operation: CANCEL() ')
            vm2.CANCEL() 

    print('Goodbye!')