print("AIDEN MCKEE, DAVID ROSALES, JOSE PEREZ, ANGEL CAHUE")
text = input('Enter Text ')
letters1 = input('Give a letter ')
letters2 = input('Give a letter ')
letters3 = input('Give a letter ')
ltext = text.lower()
print(ltext.count(letters1))
print(ltext.count(letters2))
print(ltext.count(letters3))
# ↓ is the one for counting the letters
print(text.count(''))
# ↓ is the first and last characters
print(text[0])
print(text[-1])
# ↓ prints the text in reverse order
print(text[::-1])
#Tells us if the word python is in the text
print(text.count('python') >= 1)
# hello everbody my name is markiplier