from vm import vm1, vm2 

print('Which VM machine would you like?')
print('1: VM1')
print('2: VM2')
type_vm = int(input()) 

if type_vm == 1: 
    vm1 = vm1() 

    print('Vending Machine 1') 
    print('')

    print('Menu: ') 
    print('0: create(int) ')
    print('1: coin(float) ')
    print('2: sugar() ')
    print('3: tea() ')
    print('4: latte() ')
    print('5: insert_cups(int) ')
    print('6: set_price(float) ')
    print('7: cancel() ')
    print('q: quit program ')

    print('Remember these operations! ')

    print('Vending Machine 1 Execution: ')

    ch = '1'

    while ch != 'q': 
        print('Select Operation: ')
        print('0-create, 1-coin, 2-sugar, 3-tea, 4-latte, 5-insert_cups, 6-set_price, 7-cancel, q-quit')
        ch = input()[0]

        if ch == '0': 
            print('Operation: create(int p)')
            print('Enter value of parameter p:')
            p = eval(input()) 
            vm1.create(p)
        elif ch == '1': 
            print('Operation: coin(float v)') 
            print('Enter value of parameter v: ')
            v = eval(input())
            vm1.coin(v)
        elif ch == '2': 
            print('Operation: sugar() ')
            vm1.sugar() 
        elif ch == '3': 
            print('Operation: tea() ')
            vm1.tea() 
        elif ch == '4': 
            print('Operation: latte() ')
            vm1.latte() 
        elif ch == '5': 
            print('Operation: insert_cups(int n) ')
            print('Enter value of parameter n: ')
            n = eval(input())
            vm1.insert_cups(n)
        elif ch == '6': 
            print('Operation: set_price(float p) ')
            print('Enter value of parameter p: ')
            p = eval(input())
            vm1.set_price(p)
        elif ch == '7': 
            print('Operation: cancel() ')
            vm1.cancel() 

    print('Goodbye!')

elif type_vm == 2: 
    vm2 = vm2() 