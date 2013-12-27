# Write a function inverse_graph which takes as its input the
# adjacency matrix of a graph and returns the adjacency matrix
# of the inverse graph.

def inverse_graph(graph):
    # YOUR CODE HERE
    res = list ()
    for i in range (len(graph)):
        row = list()
        for j in range (len (graph[i])):
            if i != j:
                t = 1 - graph[i][j]
            else:
                t = 0
            row.append (t)
        res.append (row)
    return res

def test():
    g1 = [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]]
    assert inverse_graph(g1) == [[0, 0, 0, 1],
                                 [0, 0, 1, 0],
                                 [0, 1, 0, 0],
                                 [1, 0, 0, 0]]
    g2 = [[0, 1, 1, 1],
          [1, 0, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 0]]
    assert inverse_graph(g2) == [[0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0]]

# If you've not seen testing like this before, all you need to do is
# to call test(). If the tests pass, you'll get no output. If they don't
# you'll get an assertion error. Don't forget to remove the call to the
# test before submitting your code.

test()
