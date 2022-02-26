import string
from queue import PriorityQueue as PriQ
import sys
def score(x, count):
    c = 0
    for i in x:
        c += count[i]
    return c
def satisfy(x, feed, guess):
    x, feed, guess= [list(x), list(feed), list(guess)]
    for i in range(5):
        if guess[i]==x[i] and feed[i]=='Y': return False
    while feed.count('G')!=0:
        i = feed.index('G')
        if guess[i]!=x[i]: return False
        else:
            guess.pop(i)
            x.pop(i)
            feed.pop(i)
    while feed.count('Y')!=0:
        i = feed.index('Y')
        if guess[i] not in x: return False
        else:
            x.pop(x.index(guess[i]))
            guess.pop(i)
            feed.pop(i)
    for i in range(len(guess)):
        if guess[i] in x: return False
    return True
def change(d, feed, guess):
    d = [x if satisfy(x, feed, guess) else '' for x in d]
    while d.count('')!=0: d.remove('')
    return d
print("Instructions:")
print("1. Enter the Suggested 5 letters in wordle game.")
print("2. Feedback is string of length 5 (R = Grey, G = Green, Y = Yellow) Ex: RYYYG.")
print("3. If 'word not in list' type 'n' in feedback.")
print("4. If you want to exit type 'q' in feedback.")
print()
alph = list(string.ascii_uppercase)
f = open("dict.txt", "r+")
d = []
for line in f:
    d.append(line.strip("\n").upper())
f.close()
count = dict()
for i in d:
    for j in i:
        if j not in alph:
            d.remove(i)
            break
        if j in count: count[j] += 1
        else: count[j] = 1
for i in range(1, 7):
    q = PriQ()
    for key in d: q.put((-score(key, count), key))
    if q.empty(): sys.exit("No word found in dictionary!!")
    print("--------------------------------------")
    print("Round", i)
    print()
    feed = 'n'
    while feed=='n':
        if i!=1: a, guess = q.get()
        else: guess = 'CRANE' 
        print(guess, end='')
        print()
        feed = input("Feedback: ")
        print()
        if feed=='GGGGG': sys.exit("Congratulations!!")
        if feed=='n': d.remove(guess)
        if feed=='q': sys.exit("Exited!")
    d = change(d, feed, guess)
sys.exit("Sorry, Please try Manually!")