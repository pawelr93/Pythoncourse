def ask(prompt):
    return int(input(prompt))


#temperature=ask('Please give me your temperature of body ?')


while True:
    temperature = ask('Please give me your temperature of body ?')
    if temperature<20:
        print('cold')
        break
    elif temperature in range(20,30):
        print('medium')
        break
    elif temperature >30:
        print('hot')
        break
    else:
        print('mistake, try again :). You have to input only number')

#while True:

    #number = ask('Give me your number ')
    # number=int(number)
    # #if number==type(int):
    #
    #     while number==1
    #
    #             score=number*(number-a)
    #             print(score)

    #else:
    #print('GIVE ME NUMBER,only')



