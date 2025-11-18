#Exercice 13
class GrapheM:
    def __init__(self,N):
        self.n = N
        self.adj = [[False for _ in range(N)] for _ in range(N)]
        self.couleur = {}
        for s in self.adj:
            self.couleur[s]="BLANC"

    def ajouter_arc(self,s1,s2):
        if (s1 < 0 or s1 > self.n) or (s2 < 0 or s2 > self.n):
            self.adj.append([False for _ in range (self.n +1)])
            for i in range (len(self.adj)):
                self.adj[i].append([False])
            self.n += 1
        self.adj[s1][s2]= True
        return self.adj
    
    def arc(self,s1,s2):
        return self.adj[s1][s2] == True

    def voisins(self,s):
        res = []
        for i in range(len(self.adj[s])):
            if self.adj[s][i] == True:
                res.append(i)
        return res

    def afficher(self,N):
        for i in range(N):
            print(i,sep=" ")
            print("->",sep=" ")
            for j in range(N):
                if self.adj[i][j]==True:
                    print(j,sep=" ")
    def degre(s):
        arc_issus = 0
        for j in range(self.n):
            if self.adj[s][j]==True:
                nb_arc+=1
        return arc_issus

    def nb_arcs(self):
        nb_arc = 0
        for s in self.adj:
            nb_arc += degre(s)
        return nb_arcs

    def supprimer_arc(s1,s2):
        self.adj[s1][s2]==False
        self.adj[s2][s1]==False
        
            

#Exercice 14

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

    def afficher(self,s):
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


#Implémentation d'un graphe orienté pondéré

class GPmat:
    def __init__(self,n):
        self.n = n
        self.adj = []#matrice d'adjacence augmentée

    def ajouter_arc(self,s1,s2,poids):
        self.adj[s1][s2] = poids

    def arc(self,s1,s2):
        if (abs(self.adj[s1][s2])== float('inf') or self.adj[s1][s2] == 0):
            return False
        return True

    def voisins(self,s):
        res = []
        for i in range (len(self.adj[s])):
            if arc(s,self.aj[i]):
                res.append((i,self.adj[i]))
        return res

    
            
            
    

class GPdict:
    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self,s):
        self.adj[s] = []
        #return self.adj

    def ajouter_arc(self,s1,s2, poids):
        if s1 in self.adj:
            self.adj[s1].append((s2,poids))
        else:
            self.adj[s1] = [(s2,poids)]
        #return self.adj

    def arc(self,s1,s2,poids):
        for tup in self.adj[s1]:
            if tup[0]==s2:
                return True
        return False

    def voisins(self,s):
        if s in self.adj:
            return list(self.adj[s])
        else:
            raise ValueError("le sommet entré n'est pas dans le graphe")
        
            
#Exercice 15
#Voir plus haut. 


###Cours
    

def parcours_prof(g,vus,s):#vus est un ensemble
    """parcours en profondeur de g depuis le sommet s"""
    if s not in vus:
        vus.add(s)
        for v in g.voisins(s):
            parcours_prof(g,vus,v)

def parcours_prof_ite(g,vus,s):
    pile = Pile(None)
    pile.empile(s)
    while not pile.est_vide():
        s=pile.depile()#on enlève le sommet de départ
        if s in vus:
            continue
        vus.add(s)
        for v in g.voisins(s):
            pile.empile(v)
                                

def profondeur(g,s):
    vus = []
    for s in g.adj:
        vus.append(s)
    return vus


#Parcours en profondeur pour trouver un cycle
def parcours_cycle(graphe,vus,s):
    visites = profondeur(graphe,s)
    cycle = False
    for i in range(len(visites)-1,-1,-1):
        if visites[i]==s:
            if graphe.couleur[visites[i-1]]=="BLANC":
            cycle = True
    return cycle


#Correction
#def parcours_cycle(g:GrapheD, couleur, s)

def floyd_Warhsall(g):
    r = g.nb_sommets
    dist = [[g.adj[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        dist[i][j]=0
    for k in range(n):
        for j in range(n):
            for i in range(n):
                x = dist[i][k]+dist[k][j]
                if x < dist[i][j]:
                    dist[i][j]=x
    return dist



        
            


            
