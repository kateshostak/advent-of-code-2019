import itertools
import pdb

class Moon():
    def __init__(self, coor, velocity):
        self.position = coor
        self.velocity = velocity

    def get_pot_energy(self):
        return sum([abs(elem) for elem in self.position])

    def get_kin_energy(self):
        return sum([abs(elem) for elem in self.velocity])

    def get_total_energy(self):
        return self.get_pot_energy()*self.get_kin_energy()

    def update_velocity(self, other_moon):
        for i in range(len(self.velocity)):
            if self.position[i] > other_moon.position[i]:
                self.velocity[i] -= 1
            elif self.position[i] < other_moon.position[i]:
                self.velocity[i] += 1


    def update_position(self):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

    def __repr__(self):
        return f'position::{self.position}, velocity::{self.velocity}'



class System():
    def __init__(self):
        self.moons = []

    def add_moon(self, coor, velocity):
        moon = Moon(coor, velocity)
        self.moons.append(moon)

    def apply_gravity(self):
        for pair in itertools.combinations(self.moons, 2):
            pair[0].update_velocity(pair[1])
            pair[1].update_velocity(pair[0])

    def apply_velocity(self):
        for moon in self.moons:
            moon.update_position()

    def step(self):
        self.apply_gravity()
        self.apply_velocity()

    def get_total_energy(self):
        return sum([moon.get_total_energy() for moon in self.moons])


def main():
    moons = [[15, -2, -6], [-5, -4, -11], [0, -6, 0], [5, 9, 6]]
    velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #moons = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
    #moons = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
    my_system = System()
    for moon, velocity in zip(moons, velocities):
        my_system.add_moon(moon, velocity)

    for i in range(1000):
        my_system.step()

    print(my_system.get_total_energy())

if __name__ == '__main__':
    main()
