import random


class Genom:

    def __init__(self, arg):
        if isinstance(arg, int):
            self.sz = arg
            self.gene = [[0, 0, 0]] * arg
            self.fitness = 0
        else:
            self.sz = len(arg)
            self.gene = arg
            self.fitness = 0

    def random_init(self):
        for i in range(len(self.gene)):
            self.gene[i] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        #self.gene = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range (self.sz)]

    def mutation(self, chance = 10):
        #todo force chance to be in [1, 1000]
        for i in range(len(self.gene)):
            if random.randint(1, 1000) <= chance:    #we do have mutation
                #print("Mutation!")

                #decide which direction
                direction = random.randint(0, 1)
                if direction == 0:
                    direction = -1
                #print("Direction: " + str(direction))

                #decide which color
                color = random.randint(0, 2)
                self.gene[i][color] += 10 * direction
                #print("Color: " + str(color))

                #truncate
                if self.gene[i][color] > 255:
                    self.gene[i][color] = 255
                if self.gene[i][color] < 0:
                    self.gene[i][color] = 0

def crossover(a, b, chance = 10):
    #todo add exception if genomes have different length
    c = Genom(a.gene[:a.sz] + b.gene[a.sz:])
    #maybe return the other combination?
    c.mutation(chance)
    return c

def crossover2(a, b, chance = 10):
    #todo add exception if genomes have different length
    newgene = []
    for i in range(a.sz):
        if random.randint(0, 1) == 0:
            newgene += [a.gene[i]]
        else:
            newgene += [b.gene[i]]

    c = Genom(newgene)
    #maybe return the other combination?
    c.mutation(chance)
    return c