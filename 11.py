def count_orbits(orbits):
    count = 0
    for key, value in orbits.items():
        tmp_count = 0
        while value != None:
            tmp_count += 1
            value = orbits.get(value)
        count += tmp_count
    return count

def main():
    orbits = {}
    orbits_reversed = {}
    with open('11.txt') as f:
        for line in f:
            obj, orb = line.strip().split(')')
            orbits[orb] = obj
    print(count_orbits(orbits))

if __name__ == '__main__':
    main()
