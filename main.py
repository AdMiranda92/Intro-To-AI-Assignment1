import collections
import sys

class node:
    def __init__(self, value=None, distance=None):
        self.value = value
        self.distance = distance
        self.previous = None
    
    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight

class heap:
    def __init__(self):
        self.queue = []
    
    def __len__(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, value, distance):
        new_node = node(value=value, distance=distance)
        self.queue.append(new_node)
        self.heapify()
    
    def find_node(self, value):
        for i in range(len(self.queue)):
            if self.queue[i].value == value:
                return i
        return False
    
    def heapify(self):
        try:
            for i in range(len(self.queue)):
                if self.queue[(i*2)+1].distance < self.queue[i].distance:
                    self.queue[(i*2)+1], self.queue[i] = self.queue[i], self.queue[(i*2)+1]
                if self.queue[(i*2)+2].distance < self.queue[i].distance:
                    self.queue[(i*2)+2], self.queue[i] = self.queue[i], self.queue[(i*2)+2]
        except IndexError:
            pass
    
    def pop(self):
        minimum = self.queue[0]
        self.queue[0] = self.queue[len(self.queue)-1]
        del(self.queue[len(self.queue)-1])
        self.heapify()
        return minimum

    # this function is purely for debug purposes
    def print_heap(self):
        for i in self.queue:
            print(i.value, i.distance)



def get_shortest_weighted_path(graph, start, end):
    path = []
    min_heap = heap()
    min_heap.push(start, 0)
    for i in graph.keys():
        if i != start:
            min_heap.push(i, sys.maxsize)   
    while min_heap.isEmpty() is False:
        # get the minimum node
        minimum = min_heap.pop()
        path.append(minimum)
        # get the adjacent nodes to the current minimum node
        adjacents = graph[minimum.value]
        for node, weight in adjacents.items():
            # if the adjacent node is in the min_heap the continue
            heap_node = min_heap.find_node(node)
            if heap_node is not False:
                # if the distance to the adjacent node is less than the current distance + weight, change the distance
                # value of the adjacent node and heapify again before the new minimum is popped
                if (minimum.distance + weight) < min_heap.queue[heap_node].distance:
                    min_heap.queue[heap_node].previous = minimum.value
                    min_heap.queue[heap_node].distance = minimum.distance + weight
                    min_heap.heapify()
            else:
                continue
        if minimum.value == end:
            break 
    
    # print out the information for the shortest path here
    final = path[-1]
    shortest_weight = final.distance
    shortest_path = []
    shortest_path.append(final.value)
    while final.value != start:
        final = [x for x in path if x.value == final.previous][0]
        shortest_path.insert(0, final.value)
    
    print("The shortest weighted path available from node {0} to node {1} is: ".format(start, end))
    for i in shortest_path:
        if i == shortest_path[-1]:
            print("{0}".format((i)), end=' ')
            break
        print("{0} -->".format(i), end=' ')
    print("with a weight of {0}".format(shortest_weight))


def main():
    # create an empty graph
    graph = {}
    # FOR THE PROFESSOR/GRADER, PLEASE CHANGE THIS LINE OF CODE TO THE APPROPRIATE FILE PATH
    with open(r'.\\assignment1\\ai_assignment1\\graph.txt', 'r') as f:
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
    
    while True:
        try:
            ending_node = int(input("Please enter the ending node: "))
        except ValueError:
            print("Invalid input")
            continue
        else:
            break
    
    get_shortest_weighted_path(graph, starting_node, ending_node)


if __name__ == '__main__':
    main()

