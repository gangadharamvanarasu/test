"""
## Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal
Test cases:

for 5 days: 14/29

for 10 days: 372/773

"""

def find_the_probability_to_miss_graduation_ceromony(final_list):
    total_possibilities = str(len(final_list))    
    abcent_days = [elm for elm in final_list if elm[-1] =='A']
    cerebony_abcent = str(len(abcent_days))
    return "{}/{}".format(cerebony_abcent, total_possibilities)


# now needs to build list like no A, one A, two A, andthen 3A
# PPP
# APP
# AAP
# AAA
n = int(input("Please enter the Number of days  : "))
# n = 10
com_list = []

base_str = "P"*n
com_list.append(base_str)

for i in range(1,n+1):
    base_str = "A"*i+ base_str[i:]
    com_list.append(base_str)

final_combinations = []

from sympy.utilities.iterables import multiset_permutations
for elm in com_list:
    for item in multiset_permutations(elm):
        final_combinations.append("".join(item))

# print(len(final_combinations))    
# print(final_combinations)

days_fout_conecutive_abcents = []

for elm in final_combinations:
    consecutive_abs = 0
    for cha in elm:        
        if cha == 'A':
            consecutive_abs += 1
            if consecutive_abs >= 4:
                days_fout_conecutive_abcents.append(elm)
                break
        else:
            consecutive_abs = 0

final_list = [elm for elm in final_combinations if elm not in days_fout_conecutive_abcents]
# print(len(days_fout_conecutive_abcents)) 
print("The number of ways to attend classes over N days : ", len(final_list))       

res = find_the_probability_to_miss_graduation_ceromony(final_list)
print("The probability that you will miss your graduation ceremony : " , res)


