
import random 


LOWER_CASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'        
UPPER_CASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   
PUNCTUATION = '!#$%&*+-=?@^_'                            
NON_DETERMINED_CHARS = 'il1Lo0O'
chars = ''


def till_input_is_correct(n):                      
    if n == '':
        return 'Yes'
    while n not in ('Yes', 'No'):
        print('Type Yes or No. Retry:')
        n = input()
    else:
        return n


passwords = []    #Stores the DAMN passwords!


def gen_safe_keys():     
    quantity = int(input('How many passwords do you want to generate: '))
    len_of_the_passwords = int(input('Enter the length of the passwords: '))
    digits = till_input_is_correct(input('Would you like to add some digits in your passwords? Yes or No: '))        
    upp_alph = till_input_is_correct(input('Would you like to generate passwords with upper letters included? Yes or No: '))            #PEP8 just thanked me for this shit
    lower_alph = till_input_is_correct(input('Would you like to generate passwords with lowers letters included? Yes or No: '))
    chr_include = till_input_is_correct(input('Would you like to generate passwords with symbols included? Yes or No: '))
    #non_determined_chr = till_input_is_correct(input('''Non-determined chars such as "il1Lo0O" shouldn't be there? Yes or No'''))                    Don't use this shit!
    for i in range(quantity):
        passwords.append([])        #Must be the only right thing I've done in this damn project
    for k in range(len(passwords)):
        count_digits_in_pass = 0
        if upp_alph == 'Yes':
            for p in range(random.randint(len_of_the_passwords // 5 + 1, len_of_the_passwords // 3)):          #I went crazy here
                passwords[k].append(random.choice(UPPER_CASE_LETTERS))
        if lower_alph == 'Yes':
            for h in range(random.randint(len_of_the_passwords // 5 + 1, len_of_the_passwords // 3)):          #Here as well
                passwords[k].append(random.choice(LOWER_CASE_LETTERS))
        if digits == 'Yes':
            for j in range(random.randint(len_of_the_passwords // 5 + 1, len_of_the_passwords // 3)):          #And here
                passwords[k].append(random.randint(0, 9))
                count_digits_in_pass += 1
        if chr_include == 'Yes':
            for u in range(1, len_of_the_passwords // 2):       #Nonsense
                passwords[k].append(random.choice(PUNCTUATION))
        while len(passwords[k]) != len_of_the_passwords:           #The foolest thing I've ever done in my life
            del passwords[k][-1]
    for i in range(len(passwords)):    
        for k in range(len(passwords[i])):
            print(passwords[i][k], end='')
        print()

    return 0    #Ends this whole nonsense


print(gen_safe_keys())
