n = int(input())

# makes new variable that is a dictionary, splits each 
# input, uses '_' to hold the input, then adds just the 
# entries in the phonebook, using 'n' which gives the
# number of entries
phonebook = dict(input().split() for _ in range(n))

def keyinDict():
    # since it's unknown number of queries, use while loop to get all of them
    while True:
        # get the queries one by one and test against our phonebook dict
        name = input()
        if name in phonebook:
            # using string formatting to fill in our print statement
            # "%s=%s" % (k, v) from the docs
            print('%s=%s' % (name, phonebook[name]))
        else:
            print('Not found')
keyinDict();
