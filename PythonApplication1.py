import random



words = [  "man","son","tie","micro","phone","game","name","medal","lucky","window","kybic","super","parents","pensil","dog","cat","horse","epson","first","python","mouse","list","table","hands","book","woomen","smart","phone","study","net","inter","food","sber","russia","world","house","place","doctor","beer","monkey","dark","white","black","bomba","qwerty","usuless","zero"]       

def random_w(words):
    word = random.choice(words)
    return word


def play(word):
    word = word.upper()
    used_words = set()

    cur = ""
    for b in word:
        cur += "_ "

    lives = 6
    w_len = len(word)

    while lives and w_len:                               # start of cycle

        user = input("Введи букву: ").upper()

        if(user in used_words):                          # if AGAIN
            print("Ты уже вводил эту букву, попробуй снова")
            print("Список использованных букв: ",end = "")
            for x in used_words: print(x,end = " ")
            print("Текущее слово: " + cur)

        elif(user in word):                          # if RIGHT
            used_words.add(user)
            i = 0
            for a in word:
                if user == a:
                    cur = cur[:i] + a + cur[i+1:]
                    w_len -= 1
                i += 2
            print("Текущее слово: " + cur)

        else:                                       # if NO
            used_words.add(user)
            print("Такой букву нет, попробуй снова")
            lives -= 1
            if lives == 2:
                open = int(input("Ты можешь открыть одну букву, введи номер: "))
                open -= 1
                b = word[open]
                open *= 2
                cur = cur[:open] + b + cur[open+1:]
                w_len -= 1
            print(f"Остаток жизней: {lives}")
            print("Текущее слово: " + cur)
        print("________________________________________________________________________________\n")

    if w_len == 0:
        print("WIIIN")
    else:
        print("You nave 0 lives")
        print("Загаданное слово: " + word)


    return 0

my_w = random_w(words)
play(my_w)

