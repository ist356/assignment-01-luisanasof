'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''
#uses: indefinite loops, lists /dicts, input

odd = []
even = []
num_dict = {'odd': odd, 'even': even}

while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0 and num != 0:
       even.append(num)
    elif num% 2 != 0:
        odd.append(num)
    elif num == 0:
        print(num_dict)
        break