# Program 2 of task 1 - prints all palindrome words in a paragraph

paragraph = "My name is Rohith. My dad and mom live in Bangalore. I don't know malayalam. I can drive a racecar."
ascii = [65,90, 97,122]

def palindrome(word) :      # Checks if a given word is a palindrome and if yes then prints it directly, otherwise ignores
    if word == word[::-1] : 
        print(word)


word = ''    #Temporarily stores words in the loop
words = []   #List of words from the paragraph

for x in paragraph :                       #manually splitting the paragraph into words to include all cases       
    if x in ['.',',','!','?','"', "'"] :   #If the word has punctuations, the code does't consider them a part of the word
        pass
    elif x in ('\n', '\t', ' ') :          #If there is a space (or tab or newline), the code will identify that a word has ended
        if word and word not in words :    #Removes the case of empty words
            words += [word]                
        word = ''                          #Resets the variable for the next word
    else : 
        word += x
if word :                                  #The letters of the last word may not be updated to the list, so this statement does that
    words += [word]

for x in words : 
    palindrome(x)
    
    

            
            
