import random as r  #library inclusion
#Working parameters
ProductList = {'p1': 10, 'p2': 15, 'p3': 20, 'p4': 25, 'p5': 30, 'p6': 35, 'p7': 50,
               'p8': 40, 'p9': 55, 'p10': 60, 'p11': 65, 'p12': 75, 'p13': 70, 'p14': 45}
LB = 290  #Setting lower bound 
UB = 310  #Setting Upper bound
ResultList = set()   #Empty set to store the resultlist

Iterations = 1000    #Number of iterations we want to perform

for _ in range(Iterations):
    combo_size = r.randint(2, len(ProductList) - 1) # Select combo size 
    ComboList = r.sample(list(ProductList.keys()),SetSize)  # Select number of elements from Set
    ComboList.sort()  #sorting of elements
    combo_sum = sum([ProductList[i] for i in combo_list])   # Sum the products in ColboList
    # Check the Sum Between LB and UB
    if LB <= combo_sum <= UB:
        ResultList.add(tuple(combo_list))

for result in ResultList:
    print(result)    # Print all the sets whose sum is between LB and UB

print("\nTotal Sets:", len(ResultList), "\n")   # Print total sets
