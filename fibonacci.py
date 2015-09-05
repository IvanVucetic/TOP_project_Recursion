# Write a method #fibs which takes a number and returns that many 
# members of the fibonacci sequence. Use iteration for this solution.

def fibs():
    list_ = [0, 1]
    print "Please enter the length of the fibonacci sequence: "
    n = raw_input("> ")

    try:
        n = int(n)
    except ValueError, e:
        print "You must enter a positive integer."
    
    ## MOST IMPORTANT PART ##
    if n <= 0:
        print "The length must be positive integer."
    elif n == 1 or n == 2:
        print [i for i in range(0, n)]
    else:
        list_ = [0, 1]
        while len(list_) < n + 1:
            list_.append(list_[-2] + list_[-1])
        print list_

fibs()


# Now write another method #fibs_rec which solves 
# the same problem recursively.

#def fibs_rec(n):


