class GrapheD:
    def __init__(self):
        self.adj = {}
        
    def ajouter_sommet(self,s):
        self.adj[s] = set()
        #return self.adj

    def ajouter_arc(self,s1,s2):
        if s1 in self.adj:
            self.adj[s1].add(s2)
        else:
            self.adj[s1] = set(s2)
        #return self.adj

    def arc(self,s1,s2):
        return (s2 in self.adj[s1])

    def voisins(self,s):
        if s in self.adj:
            return list(self.adj[s])
        else:
            raise ValueError("le sommet entré n'est pas dans le graphe")

    def afficher(self):
        for s in self.adj:
            print(s, sep=" ")
            print(self.adj[s])
            

    def nb_sommets(self):
        nb = 0
        for c in self.adj :
            nb+=1
        return nb

    def degre(self,s):
        degre = 0
        for s in self.adj:
            degre+=1
        return degre

    def nb_arcs(self):
        nb_arc=0
        for s in self.adj:
            nb_arc+=degre(s)
        return nb_arc

    def supprimer_arcs(s1,s2):
        self.adj[s1].remove(s2)
        self.adj[s2].remove(s1)

g1 = GrapheD()
##som = ["A","B","C","E","D"]
##for i in range(0,len(som)-1,2):
##    g1.ajouter_sommet(som[i])
##    g1.ajouter_sommet(som[i+1])
##    g1.ajouter_arc(som[i],som[i+1])
##    g1.ajouter_arc("B","D")
##    g1.ajouter_arc("B","D")
g1.adj = {"A":{"B"},"B":{"A","C","D"},"C":{"B","E"},"E":{"C","D"},"D":{"B","E"}}

g2 = GrapheD()
g2.adj = {"A":{"E"},"E":{"A","C","D"},"C":{"E","B"},"B":{"C","D"},"D":{"E","B"}}


def colorie(g):
    nb = 0
    coloriage = {}
    for s in g.adj:
        voisi = g.voisins(s)
        print(voisi)
        color = choix_couleur(voisi,coloriage)
        print(color)
        if color not in coloriage.values():
            nb+=1
        coloriage[s]=color
    return (coloriage,nb)

def choix_couleur(voisins,coloriage):
    m = len(voisins)
    dispo = [True for _ in range(m+1)]
    print(dispo, end=",")
    print("dispo")
    for i in range(m):
        if voisins[i] in coloriage:
            print(voisins[i],end=",")
            print("voisin")
            dispo[coloriage[voisins[i]]] = False
    for j in range(m):
        print(dispo[j],end=",")
        print("dispo_couleur")
        if dispo[j]:
            return j


def colorie2(g):
    nb = 0
    coloriage = {}
    S = color_diff(s)


def color_diff(
