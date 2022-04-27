

# to input a a phrase
user_input = str(input("Enter a Phrase: "))
# getting the acronym from the phrase
text = user_input.split()
a = " "
# for loop
for i in text:
    a = a+str(i[0]).upper()
print(a)
