

class Graph:
    def __init__(self):
        self.neighbors = {}

    def add_edge(self, v1, v2):
        if v1 not in self.neighbors:
            self.neighbors[v1] = set()
        self.neighbors[v1].add(v2)
    
    def __str__(self):
        return str(self.neighbors)
    
    def dfs_print(self, start):
        return self.dfs_print_helper(start, set())

    def dfs_print_helper(self, v, visited) -> None:
        if v in visited:
            return
        print(v)
        visited.add(v)
        for n in self.neighbors[v]:
            self.dfs_print_helper(n, visited)


    def bfs_print(self, start):
        visited = set()
        queue = [start]

        while len(queue) != 0:
            v = queue.pop(0)
            if v in visited:
                continue
            visited.add(v)
            print(v)
            queue += self.neighbors[v]

    def dfs(self, source, target) -> list[int] | None:
        return self.dfs_helper(source, target, set())
    
    def dfs_helper(self, source, target, visited) -> list[int] | None:
        if source in visited:
            return None
        visited.add(source)

        if source == target:
            return [target]
        
        for n in self.neighbors[source]:
            if (path := self.dfs_helper(n, target, visited)):
                return [source] + path
        
        return None
    
    def bfs(self, source, target) -> list[int] | None:
        visited = set()
        queue = [source]
        shortest_paths = {source: [source]}
        while len(queue) != 0:
            current = queue.pop(0)
            if current == target:
                return shortest_paths[target]
            visited.add(current)
            shortest_path_from_source_to_current = shortest_paths[current]
            for n in self.neighbors[current]:
                if n not in shortest_paths and n not in visited:
                    shortest_paths[n] = [*shortest_path_from_source_to_current, n]
                    queue.append(n)
        return None
    

class EdgeList:
    def __init__(self):
        self.edges = []
        self.neighbors_cache = {}

    def neighbors(self, v) -> list[int]:
        if v in self.neighbors_cache:
            return self.neighbors_cache[v]
        
        ns = []
        for v1, v2 in self.edges:
            if v1 == v:
                ns.append(v2)

        self.neighbors_cache[v] = ns
        return ns



edges = [(1, 2), (1, 3), (2, 1), (2, 3), (2, 5), (2, 6), (3, 1), (3, 2), (3, 6), (3, 4)]

g = Graph()
for e in edges:
    g.add_edge(*e)
    g.add_edge(e[1], e[0])
print(g)
print(f"{g.dfs_print(1)=}")
print(f"{g.bfs_print(1)=}")
print(f"{g.dfs(1, 1)=}")
print(f"{g.dfs(1, 6)=}")
print(f"{g.dfs(1, 10)=}")
print(f"{g.bfs(1, 1)=}")
print(f"{g.bfs(1, 6)=}")
print(f"{g.bfs(1, 10)=}")

def fib(n: int) -> int:
    if n < 0:
        raise ValueError()
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fast_fib(n: int) -> int:
    if n < 0:
        raise ValueError()
    return fast_fib_helper(n, {0: 0, 1: 1})

def fast_fib_helper(n: int, cache: dict[int, int]) -> int:
    if n in cache:
        return cache[n]
    fib_of_n = fast_fib_helper(n - 1, cache) + fast_fib_helper(n - 2, cache)
    cache[n] = fib_of_n
    return fib_of_n


def fib_bottom(n: int) -> int:
    cache = (n + 1) * [0]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]

print(f"{fib(0)=}")
print(f"{fib(1)=}")
print(f"{fib(3)=}")
print(f"{fib(5)=}")
print(f"{fib(10)=}")
print(f"{fast_fib(100)=}")
print(f"{fib_bottom(100)=}")