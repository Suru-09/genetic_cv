import os
from PIL import Image

from genetic.genom import Genom
from genetic.genom import crossover2

def getdif1(imdata1, imdata2):
    dif = 0
    for i in range(len(imdata1)):
        dif += abs(imdata1[i][0] - imdata2[i][0])
        dif += abs(imdata1[i][1] - imdata2[i][1])
        dif += abs(imdata1[i][2] - imdata2[i][2])

    return dif


def parsedir(path):
    for root, dirs, files in os.walk(path):
        for img in files:
            print("Processing " + img)
            im = Image.open(os.path.join(root, img))
            width, height = im.size
            print("Width = " + str(width), " height = " + str(height))
            imrgb = im.convert("RGB")
            imdata = list(imrgb.getdata())
            #print(imdata)

            #g1 = Genom(width * height)
            #g1.random_init()
            #g1.mutation(20)


            #print(g1.gene)

            #generate a list of genomes
            population = []
            for i in range (2000):
                temp = Genom(width * height)
                temp.random_init()
                population += [temp]

            best = 32 * 32 * 3 * 256
            for generation in range(100):
                print("Generation " + str(generation), " best score " + str(best))

                #evaluate individuals
                for individual in population:
                    individual.fitness = getdif1(individual.gene, imdata)

                #sort by fitness
                population.sort(key=lambda x: x.fitness)

                if population[0].fitness < best:
                    best = population[0].fitness
                    print("New best: " + str(best))

                #breeding
                new_gen = []
                for i in range(32):
                    for j in range(32):
                        new_gen += [crossover2(population[i], population[j], 10)]

                #keep best + new generation
                population = population[:1000] + new_gen[:1000]






def main():
    parsedir("pics")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
