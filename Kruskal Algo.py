class DisjointSet:
    def __init__(self, vertices):
        self.parent = [i for i in range(vertices)]
        self.rank = [0] * vertices

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, src, dest, weight):
        self.edges.append([src, dest, weight])

    def kruskal(self):
        self.edges = sorted(self.edges, key=lambda item: item[2])
        mst = []
        total_weight = 0

        ds = DisjointSet(self.vertices)

        for edge in self.edges:
            src, dest, weight = edge
            if ds.find(src) != ds.find(dest):
                mst.append(edge)
                total_weight += weight
                ds.union(src, dest)

        return mst, total_weight

if __name__ == "__main__":
    v = int(input("Enter number of vertices: "))
    g = Graph(v)

    e = int(input("Enter number of edges: "))
    print("Enter edges as 'source destination weight':")
    for _ in range(e):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    mst, total_weight = g.kruskal()
    print("\n------------------------")
    print("Edges in the MST:")
    for edge in mst:
        print(f"{edge[0]} -> {edge[1]} : {edge[2]}")
    print("------------------------")
    print("\n------------------------")
    print(f"Total weight of MST: {total_weight}")
    print("------------------------")