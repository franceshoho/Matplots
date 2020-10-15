import matplotlib.pyplot as plt
from random_walk import RandomWalk


def generate_random_walk():
    graph = RandomWalk()
    graph.generate_walks()
    # plot random walk
    plt.style.use("classic")
    fig, ax = plt.subplots()  # default is 1 chart
    ax.scatter(graph.x_values, graph.y_values, s=15)
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

