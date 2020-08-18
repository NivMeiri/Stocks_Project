def question1(a1, an, n):
    sn = float(n * (a1 + an) / 2)  # calculate the sum of the expression
    if n == 1:
        print(a1)  # if n==1 ,print a1
    elif n == 0:
        print("0")  # if n==0,print 0
    else:
        print(sn)  # otherwise,print the sum expression


# **************************************************************
# ************************ QUESTION 2 **************************
print(question1(10, 100, 2))


def question2(x):
    n = 1
    while (n <= x):  # the program is runing while x<n
        if (n % (3) == 0 and n % (5) == 0):
            print("GUMIGAM")  # if the number divide by 5 and 3 without remainder,the program print GUMIGAM
            n = n + 1
        elif (n % (3) == 0):
            print("SHOKO")  # if the number divide by 3 without remainder, the program print SHOKO
            n = n + 1
        elif (n % (5) == 0):
            print("BO")  # if the number divide by 5 without remainder, the program print BOO
            n = n + 1
        else:
            print(n)  # if the number is not divide by 3 or 5 without remainder,the program print the number.
            n = n + 1
    else:
        print("**********")


# **************************************************************
# ************************ QUESTION 3 **************************
def question3(s):
    word = s  # repalce the word with "s" string from the input
    n = len(word)
    if n >= 2:  # check the number of chracters.if it less then 2,the program print FALSE
        for i in range(n):
            if word[:] == word[::-1]:  # take the word and compare it to the opposite word and check if it palidrome
                print("TRUE")
                break
            else:
                s_new = word[0:i] + word[
                                    i + 1:]  # if the word isnt eqaul to the opposite word the program compare every chracter and find if it almost palindrome
                if s_new == s_new[::-1]:
                    print("TRUE")
                    break
                else:
                    if (i + 1 == n):
                        print("FALSE")
                    else:
                        i = i + 1
    else:
        print("FALSE")


# **************************************************************
# ************************ QUESTION 4 **************************
def question4(input_list):
    n = 0  # use for counter
    mylist = input_list  # define the list from "input_list"
    even_list = []
    odd_list = []
    x = len(mylist)  # check the length of the list
    for i in mylist:
        if (n < x and mylist[
            n] != 0):  # if n<lengh and the value in the list diffirent from 0 the program continue to run
            if (i % 2 == 0):
                even_list.append(i)  # add the even value to even list
                n = n + 1
            else:
                odd_list.append(i)  # add the odd value to odd list
                n = n + 1
    else:
        even_list.sort();
        odd_list.sort();
        answer = (even_list[-1] + even_list[-2] + odd_list[-1] + odd_list[
            -2]) / 4  # calculte the 2 biggest value from even list and odd list and divide by 4.
        print(answer)


def question1(a1, an, n):
    sn = float(n * (a1 + an) / 2)  # calculate the sum of the expression
    if n == 1:
        print(a1)  # if n==1 ,print a1
    elif n == 0:
        print("0")  # if n==0,print 0
    else:
        print(sn)  # otherwise,print the sum expression


# **************************************************************
# ************************ QUESTION 2 **************************
print(question1(10, 100, 2))


def question2(x):
    n = 1
    while (n <= x):  # the program is runing while x<n
        if (n % (3) == 0 and n % (5) == 0):
            print("GUMIGAM")  # if the number divide by 5 and 3 without remainder,the program print GUMIGAM
            n = n + 1
        elif (n % (3) == 0):
            print("SHOKO")  # if the number divide by 3 without remainder, the program print SHOKO
            n = n + 1
        elif (n % (5) == 0):
            print("BO")  # if the number divide by 5 without remainder, the program print BOO
            n = n + 1
        else:
            print(n)  # if the number is not divide by 3 or 5 without remainder,the program print the number.
            n = n + 1
    else:
        print("**********")

print(question2(9)  )
# **************************************************************
# ************************ QUESTION 3 **************************
def question3(s):
    word = s  # repalce the word with "s" string from the input
    n = len(word)
    if n >= 2:  # check the number of chracters.if it less then 2,the program print FALSE
        for i in range(n):
            if word[:] == word[::-1]:  # take the word and compare it to the opposite word and check if it palidrome
                print("TRUE")
                break
            else:
                s_new = word[0:i] + word[
                                    i + 1:]  # if the word isnt eqaul to the opposite word the program compare every chracter and find if it almost palindrome
                if s_new == s_new[::-1]:
                    print("TRUE")
                    break
                else:
                    if (i + 1 == n):
                        print("FALSE")
                    else:
                        i = i + 1
    else:
        print("FALSE")


# **************************************************************
# ************************ QUESTION 4 **************************
def question4(input_list):
    n = 0  # use for counter
    mylist = input_list  # define the list from "input_list"
    even_list = []
    odd_list = []
    x = len(mylist)  # check the length of the list
    for i in mylist:
        if (n < x and mylist[
            n] != 0):  # if n<lengh and the value in the list diffirent from 0 the program continue to run
            if (i % 2 == 0):
                even_list.append(i)  # add the even value to even list
                n = n + 1
            else:
                odd_list.append(i)  # add the odd value to odd list
                n = n + 1
    else:
        even_list.sort();
        odd_list.sort();
        answer = (even_list[-1] + even_list[-2] + odd_list[-1] + odd_list[
            -2]) / 4  # calculte the 2 biggest value from even list and odd list and divide by 4.
        print(answer)


def multiply(a, b):

    return (a * b)

print(multiply(2,2))

def countBits(n):
    get_bin = lambda n: format(n, 'b')
    x=get_bin(n)
    return (x.count("1"))

def likes(names):
    Arr_size=len(names)
    if (Arr_size==0):return("no one likes this")
    elif( Arr_size==1) : return  (str(names[0]+ " likes this"))
    elif( Arr_size==2) : return (str(names[0])+" and "+(str(names[1]))+ " like this")
    elif( Arr_size==3) : return (str(names[0])+", "+(str(names[1]))+" and "+(str(names[2]))+ " like this")
    else : return (str(names[0])+", "+(str(names[1]))+" and "+str(Arr_size-2)+" others like this")




def digital_root(n):
    n2=str(n)
    sum=0
    if(len(n2)==1):return n
    else:
        for i in range (len(n2)):
            sum+=int(n2[i])
        return digital_root(sum)


def digital_root1(n):
    return n%9 or n and 9
print(digital_root1(11))
print(11 and 9)


print("hello my name is shmul")
print("hello my name is shmul")
print("hello my name is shmul")
print("hello my name is shmul")
print("hello my name is shmul")