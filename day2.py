import re
from collections import Counter

from fetch_data import fetch_input


if __name__ == "__main__":

    data = fetch_input(2)[:-1]
#     data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9""".split('\n')

    # print(data)
    res = 0
    for row in data:
        print(row)
        r = list(map(int, row.split(' ')))

        r2 = [r[i+1]- r[i] for i, x in enumerate(r[:-1])]
        print(r2)
        l_pos = lambda x: 3 >= x >= 1
        l_neg = lambda x: -3 <= x <= -1
        if r2[0] < 0:
            lam = l_neg
        else:
            lam = l_pos

        r3 = list(map(lam, r2))
        print("r3", r3)
        r4 = int(all(r3))
        print(r4)
        print("")
        # if not r4:
        #     print(r)
        res += r4

    print(res)

        
        
 