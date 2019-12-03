def calculate_fuel(mass):
    if mass//3 <= 0:
        return 0
    fuel = mass//3 - 2 + calculate_fuel(mass//3 - 2)
    if fuel < 0:
        return 0
    return fuel

def main():
    total_fuel = 0
    with open('1.txt') as f:
        for line in f:
            mass = int(line)
            fuel = calculate_fuel(mass)
            total_fuel += fuel
    print(total_fuel)
if __name__ == '__main__':
    main()



