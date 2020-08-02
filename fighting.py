import re
total_test_cases=int(input())
list_of_elements=[]
r = re.compile(r'[a-zA-Z]+') 
for test_case in range(0,total_test_cases):
    element=input()
    if r.match(element):
        if len(element)<=5:
            element=element.lower()
            list_of_elements.append(element)
            removed_duplicate=list(set(list_of_elements))    ## removal of duplicates 
            length_of_list=len(removed_duplicate)
print(length_of_list)
removed_duplicate.sort()
print('\n'.join(map(str, removed_duplicate)))
