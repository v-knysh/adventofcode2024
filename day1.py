import re


from fetch_data import fetch_input


if __name__ == "__main__":

    data = fetch_input(1)[:-1]

    print(data)

    r = re.compile(r"(\d*)\s*(\d*)")
    res = 0
    l1 = []
    l2 = []

    for row in data:
        d1 = int(r.match(row)[1])
        d2 = int(r.match(row)[2])
        l1.append(d1)
        l2.append(d2)

    res = sum(abs(p[0] - p[1]) for p in zip(sorted(l1), sorted(l2)))

    print(abs(res))

        
        
 