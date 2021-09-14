userinput = input()
splitinput = userinput.split(' ')
if int(splitinput[0]) > int(splitinput[1]):
    print('>')
if int(splitinput[0]) < int(splitinput[1]):
    print('<')
if int(splitinput[0]) == int(splitinput[1]):
    print('==')
