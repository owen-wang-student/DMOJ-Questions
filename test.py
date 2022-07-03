# direct friends
graph = [[], [6], [6], [4, 5, 6, 15], [3, 5, 6], [3, 4, 6], [1, 2, 3, 4, 5, 7], [6, 8], [7, 9], [8, 10, 12], [9, 11],
         [10, 12], [9, 11, 13], [12, 14, 15], [13], [3, 13], [17, 18], [16, 18], [16, 17], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

inp = input()

while inp != "q":
    if inp == "i":  # add direct friendship
        x = int(input())
        y = int(input())
        if y not in graph[x]:
            graph[x].append(y)
        if x not in graph[y]:
            graph[y].append(x)
    elif inp == "d":  # delete direct friendship
        x = int(input())
        y = int(input())
        graph[x].remove(y)
        graph[y].remove(x)
    elif inp == "n":  # number of direct friends
        x = int(input())
        print(len(graph[x]))
    elif inp == "f":  # number of friends of friends
        x = int(input())
        friends = []
        for i in graph[x]:
            for j in graph[i]:
                if j != x and j not in graph[x]:
                    friends.append(j)
        print(len(friends))
    elif inp == "s":  # shortest path between two people
        x = int(input())
        y = int(input())
        # assign distances
    inp = input()
