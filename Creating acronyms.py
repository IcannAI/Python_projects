# To create an acronym as an abbreviation formed from initial letters of words as a new word
# To generate a short form of a given sentence by splitting and indexing method
# Taking a string user input and using the split() function for splitting the words 
user_input = str(input("Enter a Phrase:"))
text = user_input.split()
# Using a new variable 'a' to store the acronym of a phase
a = ""
# Running a for loop over the variable 'text' representing the split of user input
# Running the for loop storing the index value of str[0] of each word and turning it into an uppercase by using the upper() function
for i in text:
    a = a + str (i[0]).upper()
print(a)