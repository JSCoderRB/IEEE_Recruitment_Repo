# Program 2 of task 1 - prints all palindrome words in a paragraph

paragraph = "My name is Rohith. My dad and mom live in Bangalore. I don't know malayalam. I can drive a racecar."
ascii = [65,90, 97,122]

def palindrome(word) : 
    if word == word[::-1] : 
        print(word)


word = '' 
words = []

for x in paragraph :                       #manually splitting the paragraph into words to include all cases       
    if x in ['.',',','!','?','"', "'"] : 
        pass
    elif x in ('\n', '\t', ' ') : 
        if word and word not in words :   
            words += [word]
        word = ''
    else : 
        word += x
if word : 
    words += [word]

for x in words : 
    palindrome(x)
    
    

            
            
