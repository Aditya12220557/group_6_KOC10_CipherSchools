# function to create acronym
def str(stng):
   
    # add first letter
    oupt = stng[0]
     
    # iterate over string
    for i in range(1, len(stng)):
        if stng[i-1] == ' ':
           
            # add letter next to space
            oupt += stng[i]
             
    # uppercase oupt
    oupt = oupt.upper()
    return oupt
 
 
# input string
new = "Computer Science Engineering"
 
# output acronym
print(str(new))
 
# input string
new = "lovely professional university"
 
# output acronym
print(str(new))
 
# input string
new = "jammu & kashmir"
 
# output acronym
print(str(new))
 
