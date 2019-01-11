
def volume1(length,*lengths): 
    """ 
    Calculates hypervolume 
    Args:
        takes in one formal arg, then *args
    """
    for l in lengths:
        length *= l
    return length    

def volume2(*lengths): 
    """
    Calculates hypervolume   
    Args: 
        no formal arg, only *args    
    """
    i = iter(lengths) 
    try:
        volume = next(i)
    except StopIteration:
        print("Error: at least one argument is needed")    
    for l in i:   # note that iterator is i not lengths
        volume *= l
    return volume 

def mass_mailer(**customers): 
    """
    Uses kwargs to create mass mailer        """

    for name, email in customers.items():
        print(f"Dear {name}, your email address {email} is invalid. Please login to update")

if __name__ == "__main__":
    len1 = 1
    len2 = [2,3,4,5,6,7]
    vol1 = volume1(len1,*len2); 
    print(f"Hypervolume of {len1} and {len2} is {vol1}")
    len3 = [1, 2,3,4,5,6,7]
    vol2 = volume2(*len3) ; 
    print(f"Hypervolume of {len3} is {vol2}") 

    mass_mailer(AlexBoo="alexboo@gmail.com", BettyCass="bettyc@yahoo.com", CathyDis="discat@fastmail.com")          

    customers1 = {"Derek Eng": "deng@gmail.com",
             "Eric Fromm": "eric_f@yahoo.com",
             "Fred Goh": "fredgoh@fastmail.com"}
    mass_mailer(**customers1)

"""
(base)$ python3 args.py
Hypervolume of 1 and [2, 3, 4, 5, 6, 7] is 5040
Hypervolume of [1, 2, 3, 4, 5, 6, 7] is 5040
Dear AlexBoo, your email address alexboo@gmail.com is invalid. Please login to update
Dear BettyCass, your email address bettyc@yahoo.com is invalid. Please login to update
Dear CathyDis, your email address discat@fastmail.com is invalid. Please login to update
Dear Derek Eng, your email address deng@gmail.com is invalid. Please login to update
Dear Eric Fromm, your email address eric_f@yahoo.com is invalid. Please login to update
Dear Fred Goh, your email address fredgoh@fastmail.com is invalid. Please login to update



"""



