def is_palindrome(n):
    '''
    Functia determina daca un numar e palindrom
    :param x: numarul pe care il verificam daca e palindrom
    :return: bool; True daca e palindrom, False daca nu e palindrom
    '''
    c=n
    i=0
    while(c):
        i=i*10+c%10
        c=c//10
    if(n==i):
        return True
    return False

def test_is_palindrome():
    assert(is_palindrome(121))== True
    assert(is_palindrome(123))== False

def is_prime(n):
    '''
    Functia determina daca un numar este prim
    :param n: numarul pe care il verificam daca este prim
    :return: bool; True daca este prim sau False daca nu este
    '''
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3, n//2, 2):
        if n%i==0:
            return False
    return True

def is_superprime(n):
    '''
    Algoritmul verifica daca numarul dat este superprim
    :param n: Numarul cverificat
    :return:bool; True daca este superprim, False daca nu e
    '''

    c=n
    while(c):
        if is_prime(c) == True:
            c=c//10
        else:
            return False
    return True

def test_is_palindrome():
    assert(is_superpime(233))== True
    assert(is_superpime(237))== False


def get_largest_prime_below(n):
    '''
    Functia returneaza ultimul numar prim mai mic decat n
    :param n: Numarul in functie de care trebuie sa stabilesc cel mai apropiat numar prim, mai mic decat n
    :return: ultimul numar prim mai mic decat n
    '''
    for i in range(n-1,1,-1):
        if is_prime(i)==True:
            return i
def test_get_largest_prime_below():
    assert(get_largest_prime_below(12))==7
    assert(get_largest_prime_below(3))==2
    assert(get_largest_prime_below(25))==23

shouldRun=True
while shouldRun:
    print("1. Determinati daca un numar este palindrom:")
    print("2. Determinati daca un numar este superprim:")
    print("3. Determinati ultimul numar prim mai mic decat n")
    print("x. Iesire")
    opt=input("Alegeti optiunea:")
    if opt=="1":
        n = int(input("Dati nr:"))
        if is_palindrome(n) ==True:
            print("Numarul dat este palindrom")
        else:
            print("Numarul dat NU este palindrom")
    elif opt=="2":
        n = int(input("Dati nr:"))
        if is_superprime(n)== True:
            print("Numarul dat este superprim")
        else:
            print("Numarul dat NU este superprim")
    elif opt=="3":
        n = int(input("Dati nr:"))
        print(get_largest_prime_below(n))
    elif opt=="x":
        shouldRun=False