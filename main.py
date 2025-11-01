class Graph:
    def __init__(self, naprav=True):
        self.nodes = {}
        self.naprav = naprav
    def add_yzel(self, znachenie):
        if znachenie not in self.nodes:
            self.nodes[znachenie] = []
    def add_pyt(self, istochnik, konec):
        self.add_yzel(istochnik)
        self.add_yzel(konec)
        self.nodes[istochnik].append(konec)
        if not self.naprav and istochnik not in self.nodes[konec]:
            self.nodes[konec].append(istochnik)

def dfs(graph, starting, k=None):
    if k is None:
        k = set()
    k.add(starting)
    print(starting)
    for n in graph.nodes[starting]:
        if n not in k:
            dfs(graph, n, k)

def bfs(g, start):
    v = []
    q = [start]
    adj = g.nodes
    while q:
        node = q.pop(0)
        if node not in v:
            v.append(node)
            for n in adj.get(node, []):
                if n not in v:
                    q.append(n)
    return v

print("Введите 1, если хотите неориентированный граф, либо 2, если хотите ориентированный")
p = int(input())
if p==1:
    moy_boy = Graph(naprav=False)
elif p==2:
    moy_boy = Graph(naprav=True)

for v in input("write nodes: ").split():
    moy_boy.add_yzel(v)

print("write edges")
while True:
    l = input().strip()
    if not l:
        break
    s, d = l.split()
    moy_boy.add_pyt(s,d)
start = input()


print("Способ в глубину:")
dfs(moy_boy, start)
print()
print("Способ в ширину:")
print(bfs(moy_boy, start))