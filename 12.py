def count_way(orbits):
    you_orb = 'YOU'
    san_orb = 'SAN'
    orb_way = []
    santa_way = build_way(san_orb, orbits)
    you_way = build_way(you_orb, orbits)
    for orb in you_way:
        if orb in santa_way:
            tmp = you_way[orb] + santa_way[orb]
            orb_way.append(tmp)
    return min(orb_way)

def build_way(orb, orbits):
    value = orbits.get(orb)
    i = 0
    ways = {}
    while value != None:
        ways[value] = i
        i += 1
        value = orbits.get(value)
    return ways

def main():
    orbits = {}
    orbits_reversed = {}
    with open('11.txt') as f:
        for line in f:
            obj, orb = line.strip().split(')')
            orbits[orb] = obj
    print(count_way(orbits))

if __name__ == '__main__':
    main()
