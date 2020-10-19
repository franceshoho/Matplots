import matplotlib.pyplot as plt
from die import Die

NUM_ROLL = 1000


def main():
    die1 = Die()
    die2 = Die()

    results = roll_dice(die1, die2)
    #print(results)

    max_value = die1.num_sides + die2.num_sides
    frequencies = analyze_freq(max_value, results)
    print(frequencies)

    # visualize results using histogram
    x_values = list(range(2, max_value+1))  # make list [2... 13]

    plt.hist(results, bins=x_values)
    plt.show()



# analyze and return freq of numbers from rolls
def analyze_freq(max, results) :
    frequencies = []

    # for num in range(2, max+1) :
    #     count = results.count(num)
    #     frequencies.append(count)
    frequencies = [results.count(num) for num in range(2, max+1)]
    return frequencies

# roll dice and return list of results of the roll
def roll_dice(die1, die2) :
    # for _ in range(NUM_ROLL) :
    #     result = die1.roll() + die2.roll()
    #     results.append(result)
    results = [die1.roll() + die2.roll() for num in range(NUM_ROLL)]
    return results

if __name__ == '__main__':
    main()