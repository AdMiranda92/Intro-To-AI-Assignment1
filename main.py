import collections
import sys

class node:
    def __init__(self, value=None, weight=None):
        self.value = value
        self.weight = weight
    
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
    
    def push(self, value, weight):
        new_node = node(value=value, weight=weight)
        self.queue.append(new_node)
        self.heapify()
    
    def heapify(self):
        try:
            for i in range(len(self.queue)):
                if self.queue[(i*2)+1].weight < self.queue[i].weight:
                    self.queue[(i*2)+1], self.queue[i] = self.queue[i], self.queue[(i*2)+1]
                if self.queue[(i*2)+2].weight < self.queue[i].weight:
                    self.queue[(i*2)+2], self.queue[i] = self.queue[i], self.queue[(i*2)+2]
        except IndexError:
            pass
    
    def pop(self):
        minimum = self.queue[0]
        self.queue[0] = self.queue[len(self.queue)-1]
        del(self.queue[len(self.queue)-1])
        self.heapify()
        return minimum

    def print_heap(self):
        for i in self.queue:
            print(i.value, i.weight)



def get_shortest_weighted_path(graph, start, end):
    # TODO implement search algorithm here
    return False


def test_heap():
    new_heap = heap()
    new_heap.push(1, 100)
    new_heap.push(2, 200)
    new_heap.push(5, 25)
    new_heap.push(9, 1)
    new_heap.push(15, 800)
    new_heap.push(3, 62)
    new_heap.push(95, 0)
    new_heap.push(51, 100)
    new_heap.print_heap()

    print("Initial heap above")
    smallest = new_heap.pop()
    print("smallest weight is: {0}".format(smallest.value))
    new_heap.print_heap()
    smallest = new_heap.pop()
    print("smallest weight is: {0}".format(smallest.value))
    new_heap.print_heap()
    smallest = new_heap.pop()
    print("smallest weight is: {0}".format(smallest.value))
    new_heap.print_heap()
    smallest = new_heap.pop()
    print("smallest weight is: {0}".format(smallest.value))
    new_heap.print_heap()
    smallest = new_heap.pop()
    print("smallest weight is: {0}".format(smallest.value))
    new_heap.print_heap()
    smallest = new_heap.pop()
    print("smallest weight is: {0}".format(smallest.value))
    new_heap.print_heap()
    smallest = new_heap.pop()
    print("smallest weight is: {0}".format(smallest.value))
    new_heap.print_heap()



def main():
    # create an empty graph
    graph = {}
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
    # while True:
    #     try:
    #         starting_node = int(input("Please enter the starting node: "))
    #     except ValueError:
    #         print("Invalid input")
    #         continue
    #     else:
    #         break
    test_heap()

main()
