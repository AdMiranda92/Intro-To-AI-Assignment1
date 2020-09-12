import collections


def get_shortest_weighted_path(graph, start, end):
    # TODO implement search algorithm here
    

def main():
    # create an empty graph
    graph = {}
    with open(r'.\\assignment1\\graph.txt', 'r') as f:
        for line in f:
            # assign the 3 int values in the line to 3 variables
            start, end, weight = [int(x) for x in line.split()]

            # if the key already exists in the graph, update its value
            # otherwise, create a new key value pair
            if start in graph:
                graph[start].update({end: weight})
            else:
                graph[start] = {end : weight}
    # for key,value in graph[1].items():
    #     print(key, value)

    # get the start and end nodes
    while True:
        try:
            starting_node = int(input("Please enter the starting node: "))
        except ValueError:
            print("Invalid input")
            continue
        else:
            break

main()
