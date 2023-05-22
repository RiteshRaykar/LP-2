import queue as Q

# Heuristic values for Maharashtra cities (you can modify them accordingly)
dict_hn = {
    'Mumbai': 0,
    'Pune': 120,
    'Solapur': 270,
    'Kolhapur': 400,
    'Thane': 50
}

# Graph of Maharashtra cities and their distances
dict_gn = {
    'Mumbai': {'Pune': 150, 'Thane': 20},
    'Pune': {'Mumbai': 150, 'Solapur': 250},
    'Solapur': {'Pune': 250, 'Kolhapur': 300},
    'Kolhapur': {'Solapur': 300},
    'Thane': {'Mumbai': 20}
}

start = str(input("Enter start city: "))
goal = str(input("Enter goal city: "))
result = ''


def get_fn(citystr):
    cities = citystr.split(" , ")
    hn = gn = 0
    for ctr in range(0, len(cities) - 1):
        gn = gn + dict_gn[cities[ctr]][cities[ctr + 1]]
        hn = dict_hn[cities[len(cities) - 1]]
    return (hn + gn)


def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get()
    if thiscity == goal:
        result = citystr + " : : " + str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr + " , " + cty), citystr + " , " + cty, cty))
    expand(cityq)


def main():
    cityq = Q.PriorityQueue()
    thiscity = start
    cityq.put((get_fn(start), start, thiscity))
    expand(cityq)
    print("The A* path with the total is: ")
    print(result)


main()