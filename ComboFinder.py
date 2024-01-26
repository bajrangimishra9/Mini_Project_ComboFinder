import random as r

ProductList = {'p1': 10, 'p2': 15, 'p3': 20, 'p4': 25, 'p5': 30, 'p6': 35, 'p7': 50,
               'p8': 40, 'p9': 55, 'p10': 60, 'p11': 65, 'p12': 75, 'p13': 70, 'p14': 45}
LB = 290
UB = 310
ResultList = set()

Iterations = 1000

for _ in range(Iterations):
    combo_size = r.randint(2, len(ProductList) - 1)
    combo_list = r.sample(ProductList.keys(), combo_size)
    combo_sum = sum(ProductList[i] for i in combo_list)
    if LB <= combo_sum <= UB:
        ResultList.add(tuple(combo_list))

for result in ResultList:
    print(result)

print("\nTotal Sets:", len(ResultList), "\n")
