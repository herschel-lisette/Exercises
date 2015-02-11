print ("I. Easy section \n") 
#Python program to find the
# H.C.F of two input number

# define a function
def hcf( x, y ):

    """This function takes two
    integers and returns the H.C.F"""

    # choose the smaller number
    if x > y:
    
        smaller = y
    
    else:
    
        smaller = x

    #-- END check to find smaller number --#

    # loop over integers from 1 to the smaller number.
    for i in range( 1, smaller + 1 ):

        # see if each divided by the other results in no remainder (% = modulo operator - remainder part of a division)
        if ( ( x % i == 0 ) and ( y % i == 0 ) ):

            # this is a common factor.  Store it, but also keep looking,
            #    in case there is a greater one.
            hcf = i

        #-- END check to see if HCF --#

    #-- END loop over integers from 1 to smaller of the two numbers --#

    return hcf

#-- END function hcf() --#

# take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

# OR just enter the numbers you want here
num1 = 72
num2 = 9

print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) + ". \n \n")


### Start the second part
print ("II. Less Easy\n")
#start with a list of numbers
num_list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Initialize 2 variables
sumof_list=0
countof_list=0

#Looping. For each, add the current number to the sum and add 1 to the counter.
for i in num_list:
	sumof_list= sumof_list+num_list[i-1]
	countof_list=countof_list+1
	
# End the loop

#Divide the sum by the count to get the mean
#Cast variables as floats to avoid integer arithmetic (i.e. dropping the decimals)
dvd=float(sumof_list)/float(countof_list)

#Output the mean
print ("The list I have is num_list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].\n"+
	"The sum of the list is "+ str(sumof_list) +".\n"+
	"The count of items in the list is " + str(countof_list)+ ".\n"+
	"The mean is " + str(dvd) +". \n \n"
	)




### Start the third part
print ("III. Advanced\n")
# Translate the binary search algorithm from PHP to Python


#define a function for a comparative binary search
def binary_search(x, lista, left, right):
	if left> right:
		return -1
		
	mid= (left+right) >>1
	if lista[mid] == x:
		return mid
	if lista[mid] > x:
		return binary_search(x, lista, left, mid-1)
	if lista[mid] < x:
		return binary_search(x, lista, mid+1, right)

#define second function for an iterative binary search
def iterative_binary_search(x, lista):
	left=0
	right=len(lista)-1
	
	while left <= right:
		mid = (left+right)>>1
		
		if lista[mid] == x:
			return mid
		if lista[mid] > x:
			right= mid-1
		if lista[mid] < x:
			left= mid+1
		
	return -1

#Test the functions
lista= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
x= 55
Lft=0
RGT=len(lista)-1
iterative_binary_search(x, lista)
binary_search(x, lista, Lft, RGT)
lista[10]
print ("lista= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]\n"+
		"x=55 \n"+
		"Using the binary search, the position for x=55 is "+ str(binary_search(x, lista, Lft, RGT))+".\n" +
		"Using the iterative search,the position for x=55 is " + str(iterative_binary_search(x, lista) )+".\n"+
		"To check what is in position 10, we see that the function lista[10] gives us "+ str(lista[10]) +".\n"
		)

#Check to see what happens if I searched for something not on the list
x=49
iterative_binary_search(x, lista)
binary_search(x, lista, Lft, RGT)
#Returns -1 which is correct.

print (	"To check to see whether the false statements are indeed returning -1, let x=49.\n"+
		"Using the binary search, the position for x=49 is "+ str(binary_search(x, lista, Lft, RGT))+".\n" +
		"Using the iterative search,the position for x=49 is " + str(iterative_binary_search(x, lista) )+"."
		)




