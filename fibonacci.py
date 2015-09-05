# Write a method #fibs which takes a number and returns that many 
# members of the fibonacci sequence. Use iteration for this solution.

def fibs():
    list_ = []
    print "Please enter the length of the fibonacci sequence: "
    n = raw_input("> ")

    try:
        n = int(n)
    except ValueError, e:
        print "You must enter a positive integer."
    
    if n <= 0:
        print "The length must be positive integer."
    elif n == 1:
        list_.append(0)
        print list_
    elif n == 2:
        list_.extend([0, 1]) # unlike append allows multiple elements
        print list_
    else:
        list_ = [0, 1]
        for i in range(3, n+1):
            new_elem = list_[i-3] + list_[i-2] # prvi elem je zapravo nulti
            list_.append(new_elem)
        print list_

#fibs()