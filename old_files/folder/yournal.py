alpha = [['a','1'],['b','2'],['c',''],['d','4'],['e','5'],['f','6'],['g','7'],['h','8'],['i','9'],['j','10'],['k','11'],['l','12'],['m','13'],['n','14'],['o','15'],['p','16'],['q','--'],['r','17'],['s','18'],['t','19'],['u','20'],['v','21'],['w','2121'],['x','--'],['y','22'],['z','--']]

word = []
hidden_word = ''
english = ''
run = True
while run == True:
    x = input('ENTER: ')

    if x == 'clear':
        conf = input("Are you sure you want to clear page?: ").lower()
        if conf == 'yes':
            with open('folder/saved_info.txt', 'w') as destination:
                destination.write('')
        else:
            pass
    
    elif x == 'done':
        save = input('Do you want to save page?: ')
        if save == 'yes':
            for i in range(len(word)):
                for char in word[i]:
                    if char == ' ':
                        hidden_word += ' '
                        pass
                    else:
                        for letter in range(len(alpha)):
                            if char == alpha[letter][0]:
                                hidden_word += alpha[letter][1] + '.'
            
            word = []              
            with open('folder/saved_info.txt', 'a') as destination:
                destination.write(hidden_word + '\n')
    
    elif x == 'read':
        password = input('What is the password?: ')
        if password == 'wizzy':
            with open('folder/saved_info.txt', 'r') as source:
                data = source.read()
            print(data)
            trans_2_eng = input('Would you like to translate?: ')
            if trans_2_eng == 'yes':
                next_password = input('ENTER: ')
                if next_password == 'wizzy':
                    #split_data = data.split()
                    for i in range(len(data)):
                        for z in range(len(data[i])):
                            print(data[i][z])
                            for x in range(len(alpha)):
                                if data[i][z] == alpha[x][1]:
                                    english += alpha[x][0]
                                elif data[i][z] == ' ':
                                    english += ' '
                                elif data[i][z] == '.':
                                    pass
                        print(english)

    elif x == '':
        pass

    else:
        word.append(x + ' ')
        
    