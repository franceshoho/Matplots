import matplotlib.pyplot as plt
from random_walk import RandomWalk


def generate_random_walk():
    graph = RandomWalk()
    graph.generate_walks()
    # plot random walk
    plt.style.use("classic")
    fig, ax = plt.subplots()  # default is 1 chart

    # se color map to generate color.  cmap requires c and cmap as args
    # c must be 1) seq of number specified by length n
    #2) an array 3) single color format string, in this case, we use 1)
    color_numbers = range(graph.num_points)
    ax.scatter(graph.x_values, graph.y_values, s=15, c=color_numbers,
               cmap='PuBuGn', edgecolors='none')
    plt.show()

def main():
    while True:
        generate_random_walk()
        answer = input("Do you want another graph? y/n  ")
        if answer.lower() == 'n':
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

