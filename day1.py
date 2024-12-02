import re
from collections import Counter

from fetch_data import fetch_input


if __name__ == "__main__":

    data = fetch_input(1)[:-1]

    print(data)

    r = re.compile(r"(\d*)\s*(\d*)")
    l1 = []
    l2 = []

    for row in data:
        d1 = int(r.match(row)[1])
        d2 = int(r.match(row)[2])
        l1.append(d1)
        l2.append(d2)

    c = Counter(l2)
    res = sum(x*c[x] for x in l1)

    print(res)

        
        
 