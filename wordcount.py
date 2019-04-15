# put your code here.
#from string import ascii_letters 
def unpack_file():  
    the_file = open("test.txt")
    total_words = []
    for line in the_file:
        line = line.rstrip()
        #line = line.strip(ascii_letters)
        words = line.split(' ') 

        for word in words:
            total_words.append(word.lower())
    return total_words

#print (total_words)

def generate_word_count():
    total_words = unpack_file()
    word_count = {}
    for key in total_words: 
        word_count[key] = word_count.get(key,0)+1
    for key in word_count:
        print (key, word_count[key])
    #return word_count


print(generate_word_count())

        