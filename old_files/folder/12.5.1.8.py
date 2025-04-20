decode = [['a','1'],['b','2'],['c',''],['d','4'],['e','5'],['f','6'],['g','7'],['h','8'],['i','9'],['j','10'],['k','11'],['l','12'],['m','13'],['n','14'],['o','15'],['p','16'],['q','--'],['r','17'],['s','18'],['t','19'],['u','20'],['v','21'],['w','2121'],['x','--'],['y','22'],['z','--']]

word = ''
all_words = []
run = True
combined = ''
decoded = ''
data = ''
def trans_eng():
    global decoded
    global decode
    global data
    for i in range(0,len(data)):
        if data[i] == ' ':
            decoded += ' '
        for z in range(0,len(decode)):
            if data[i] == decode[z][1]:
                decoded += decode[z][0] 

    print(f'decode: {decoded}')
def trans_num():
    global all_words
    global combined
    global decoded
    global decode
    global data
    s = ''
    for i in range(0,len(all_words)):
        s += all_words[i] + ' '
    for char in s:
        for i in range(0,len(decode)):
            if char == decode[i][0]:
                combined += decode[i][1] + '.'
    print(combined)
    return combined



while run == True:
    x = input('ENTER: ')

    if x == '':
        word = word[0:count_letters(word)-1]
        word += ' '
        all_words.append(word)
        word = ''

    elif x == 'clear':
        conf = input("Are you sure you want to clear page?: ").lower()
        if conf == 'yes':
            with open('folder/saved_info.txt', 'w') as destination:
                destination.write('')
        else:
            pass
    elif x == 'done':
        #for i in range(0,len(all_words)):

            #combined += all_words[i]
        #print(combined)
        trans_num()
        save = input('Save Notes?: ').lower()
        if save == 'yes':
            with open('folder/saved_info.txt', 'a') as destination:
                destination.write(f'{combined}' + '\n')
        else:
            pass
    if x == 'read':
        with open('folder/saved_info.txt', 'r') as source:
            data = source.read()
            print(data)
            for i in range(0,len(data)):
                if data[i] == '.':
                    pass
            trans_eng()
            trans_num()

        run = False
    else:
        word += x
