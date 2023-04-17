word = input("What word would you like to check if it's a Palimdrome? ")

reversed_word = word[::-1]

if(word == reversed_word):
    print("Yes, the word " + word + " is a Palimdrome")
else:
    print("No, the word " + word + " is not a Palimdrome")