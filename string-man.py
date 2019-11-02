print("""
    STRING MANIPULATION
    print_items_in_a_list(list_1)
    print_items_in_range(x,y)
    abbrevName(name)
    print_string(a)
      """)

def print_string(a):
    """
    :param a: str.
    :return:
    """
    a = str(input("Please enter a string: "))
    print(a)
    
def print_items_in_a_list(list_1):
    #list_1 = ["Blessed Assurance", "At Calvary", "New Name", "Onward"]
    x = len(list_1)
    n = 0
    while n < x:
        print (list_1[n])
        n += 1


def print_items_in_range(x,y):
    for n in range(x,y):
        return(n)


def challenge_3():
    list_1 = ["Blessed Assurance", "At Calvary", "New Name", "Onward"]
    x = len(list_1)
    n = 0
    while n < x:
        y = list_1[n]
        print(n, "-" , y)
        n += 1
        
        
def infin():
    nos = [1,2,3,4,5,6,7,8,9,0]
    while True:
        try:
            g = int(input("Guess a number: "))
        
            if g in nos:
                print ("Correct!!")
            else:
                print("Wrong!!")
            q = input("Type q to quit!!: ")
            if q == "q":
                break
        except ValueError:
            return ("Please enter an integer!!")


    
def abbrevName(name):
    name = name.split(" ")
    hi = list()
    for i in range (len(name)):
        a = name[i]
        initial = a[0:1]
        initial = initial.upper()
        hi.append(initial)
    return (hi[0] + "." + hi[1])

'''
    Forever
    Author of Salvation
    My God is might to save
    He is mighty to save!!!
'''

