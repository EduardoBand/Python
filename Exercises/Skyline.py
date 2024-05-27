#Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

#OR

def myfunc2(word):
    word_letter =[]
    for letter in range(len(word)):
        if (letter+1) % 2==0:
            word_letter+=word[letter].upper()
        else:
            word_letter+=word[letter].lower()
    return word_letter

print(myfunc2('Hello'))