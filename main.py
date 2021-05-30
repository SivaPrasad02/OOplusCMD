from methods.classes import *

def print_():
    print('\n')
    print('Enter the Option you :')
    print('1. Create an object')
    print('2. Delete an object with given name')
    print('3 Run the execute funtion to see the object created with class name')
    print('4 Get the count of Object and classes invoked ')
    print('Q For quit')

def Process():
    count_of_obj = {}
    count_of_class = {}
    print_()
    lst = {}
    #Option = input('Enter the Option : ')
    while True:
        Option = input('Enter the Option : ')
        if Option == '1':
            cls = input('Enter the Class you want to create : ')
            if cls =='A':
                Input =  input('Enter the variable you want to create an object : ')
                st = Input
                Input = A(Input)
                count_of_class['A'] =0
                count_of_obj[st] = 0
                lst[st]  =  Input
                print_()
            elif cls =='B':
                Input =  input('Enter the variable you want to create an object : ')
                st = Input
                Input = B(Input)
                count_of_class['B'] =0
                count_of_obj[st] = 0
                lst[st]  =  Input
                print_()
            elif cls =='C':
                Input =  input('Enter the variable you want to create an object : ')
                st = Input
                Input = C(Input)
                count_of_class['C'] =0
                count_of_obj[st] = 0
                lst[st]  =  Input
                print_()
            else:
                print('Give input of Valid  Class')
                print('We have Only Classes OF  A, B, C')


        elif Option == '2':
            Del_input = input('Enter the object you want to delete :')
            print('Deleting the object : {}'.format(Del_input))
            try:
                del lst[Del_input]
            except:
                print('Delete the objects that you created')
            print_()

        elif Option == '3':
            print('These are the you objects You created ')
            for i in lst:
                print(i)
            run_obj = input('Enter the object you want to Run Created before: ')
            try:
                cls_ = lst[run_obj].execute()

                count_of_obj[run_obj]  = count_of_obj[run_obj] +1
                count_of_class[cls_] = count_of_class[cls_]+1
            except:
                print('Invoke the Objects created Only')
        elif Option=='4':
            for i in count_of_obj.keys():
                print('The No of times object "{}" Invoked are {}'.format(i,count_of_obj[i]))
            for i in count_of_class.keys():
                print('The No of times CLass "{}" Invoked are {}'.format(i,count_of_class[i]))

            print_()
        elif Option=='q':
            break

Process()