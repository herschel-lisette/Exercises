#store filename as romeo
romeo="pg1513.txt"

#open the romeo file as a read-only access
open_romeo=open(romeo, "r")

#Initialize the counter variables.
numberOfWords=0
numberOfLines=0
numberOfChars=0
totalText=""
totalChar=""
# Start looping through the text file.
for current_line in open_romeo:
    #Lower case, strip white space, take out commas
    lower_string=current_line.lower()
    strip_string=lower_string.strip()
    no_comma=strip_string.replace(","," ")
    #Create a list of words per line
    words=no_comma.split()
    #Combine all the lines together, this will be used later for the dictionary.
    totalText+=" "+no_comma
    totalChar+=no_comma
    
    #Length of words per line as well as length of characters per line
    currentStringCount=len(words)
    currentCharCount=len(no_comma)
    
	#Create a counter for number of lines, words, and characters
    numberOfLines+=1
    numberOfWords+=currentStringCount
    numberOfChars+=currentCharCount
    
# End the loop

#Print the number of lines, words, and characters in the document.
print("Number of lines in the document is: "+ str(numberOfLines)+ ".\n" )
print("Number of words in the document is: "+ str(numberOfWords)+ ".\n")
print("Number of characters in the document is: "+ str(numberOfChars)+ ".\n")


#Another way to get the total number of characters
print("The other method of getting the number of characters also gives us: " + str(len(totalChar)) +" number of characters. \n")
#Another way to get the total number of words
totalWords=totalText.split()
print("The other method of getting the number of words also gives us: " + str(len(totalWords)) +" number of words. \n")

#Make sure the text is all in one line. No paragraph marker or anything like that.
print(totalText+ "\n")


#### Try and do the second part of the project: Word count
#Initialize dictionary
dictionaryWords={}
counter=0

##Remove the extra stuff to make sure extra stuff next to a word does not make it a unique word.
#Remove period, exclamation point, question mark, brackets, parenthesis, asterisk.
no_period=totalText.replace("."," ")
no_ex=no_period.replace("!"," ")
no_br= no_ex.replace("["," ")
no_br2= no_br.replace("]"," ")
no_p= no_br2.replace(")"," ")
no_p2= no_p.replace("("," ")
nodash=no_p2.replace("-"," ")
no_q=nodash.replace("?"," ")
no_a=no_q.replace("*"," ")

#Split the text and make it into a list of words.
wordsx=no_a.split()

#Create loop that checks whether word is in dictionary or not. If not in dictionary, add it and say value is 1. If it is in the dictionary, increment the value by 1.
for current_word in wordsx:
    if (current_word in dictionaryWords):
        #Current word in dictionary, get its value
        value_word=dictionaryWords[current_word]
        dictionaryWords[current_word]=value_word+1
                
    else:
        #If current word not present, add it to dictionary
        dictionaryWords[current_word]=1
    
	#Create counter to check if program is still running.
    counter+=1
    if (counter%1000)==0:
        print(counter)
#End loop


print("\n")   
#Print the number of unique words using the method implemented.     
print("The number of unique words in the dictionary is "+ str(len(dictionaryWords))+".\n")
#Print first and last items in dictionary.
print("The first item in the dictionary is: "+ str(dictionaryWords.items()[0])+ ".\n")
print("The last item in the dictionary is: " +str(dictionaryWords.items()[4780])+ ".\n")
#Print all of the dictionary items.
print("The dictionary items are the following: \n"+ str(dictionaryWords))