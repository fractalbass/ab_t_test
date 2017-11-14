import numpy as np
import matplotlib.pyplot as plt
import random

np.random.seed(19680801)
#np.random.seed(46)

class DataSimulator():

    def get_random_sale(self, type):

        result = [-1]
        if type=="A":
            i = np.random.randint(0, 100)
            if i < 20:
                result = np.random.normal(350, 8.0, 1)

        if type == "B":
            i = np.random.randint(0, 100)
            if i < 30:
                result = np.random.normal(355, 8.0, 1)
        return result[0]

    def simulate(self):
        print("Simulating...")
        x = list()
        y = list()
        length = 100
        for i in range(0,length):
            a = self.get_random_sale("A")
            if a > 0:
                x.append(a)

            b = self.get_random_sale("B")
            if b > 0:
                y.append(b)

        print("Treatment\t ")

        print("Number of impressions: {0}".format(length))
        print("Length of A: {0}".format(len(x)))
        print("Average A sale: {0}".format(np.average(x)))
        print("Length of B: {0}".format(len(y)))
        print("Average B sale: {0}".format(np.average(y)))
        print("Simulation done.  Plotting...")

        print("A values...")
        for m in x:
            print(m)

        print("B values...")
        for n in y:
            print(n)

        # print ("----------")
        #
        # # the histogram of the data
        n, bins, patches = plt.hist(x, 50, normed=0, facecolor='g', alpha=0.75)
        n, bins, patches = plt.hist(y, 50, normed=0, facecolor='b', alpha=0.75)
        plt.xlabel('Price')
        plt.ylabel('Count')
        plt.title('Histogram of Siumlated Sales')
        # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        # plt.axis([40, 160, 0, 0.03])
        plt.grid(True)
        plt.show()



if __name__ == "__main__":
    ds = DataSimulator()
    ds.simulate()
