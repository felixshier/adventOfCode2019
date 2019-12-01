from math import floor


def calcFuel(x):
    return floor(x/3)-2


def calcTotalFuel(x):
    fuel = calcFuel(x)
    if fuel > 6:
        fuel = fuel + calcTotalFuel(fuel)
    return fuel


if __name__ == "__main__":

    f = open(r"C:\Users\Felix\Documents\adventOfCode\dayOneInput.txt", "r")
    moduleMasses = []
    for x in f:
        moduleMasses.append(int(x))

    #day 1 part 1
    fuelReq = [calcFuel(mass) for mass in moduleMasses]
    fuelReqSum = sum(fuelReq)
    print("Initial fuel required: {}".format(fuelReqSum))
    #day 1 part 2
    totalFuelReq = [calcTotalFuel(mass) for mass in moduleMasses]
    totalFuelReqSum = sum(totalFuelReq)
    print("Actual fuel required: {}".format(totalFuelReqSum))





