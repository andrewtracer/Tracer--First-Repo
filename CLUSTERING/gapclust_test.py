import csv, re, math
from scipy import stats
from types import *
from numpy import *
from random import *
import pickle

pwy_file  = "./pwy_sets.pkl"

pwy_data = open(pwy_file, 'rb')
pwys = pickle.load(pwy_data)

class Path:
    def __init__(self, name, genes_vector):
        self.name = name
        self.gvect = genes_vector
    def jac(self, other):
        return 1.0 - double(inner(self.gvect,other.gvect)) / double(min(sum(self.gvect),sum(other.gvect))) * double(max(sum(self.gvect),sum(other.gvect))) / double((sum(self.gvect+other.gvect) - inner(self.gvect,other.gvect)))
    def __str__(self):
        return self.name

def getBasis(pwys):
    b_genes = set()
    for i in range(len(pwys)):
        b_genes = b_genes.union(set(pwys[i][1]))
    return b_genes

def genetoNum(pwys, basis):
    num_pwys = []
    for i in pwys:
        new_pwy = []
        for j in basis:
            toadd = False
            if j in set(i[1]):
                toadd = True
            if toadd:
                new_pwy.append(1)
            else:
                new_pwy.append(0)
        num_pwys.append([i[0], new_pwy])
    return num_pwys


def sendtoClass(pwys):
    for i in range(len(pwys)):
        pwys[i] = Path(pwys[i][0],pwys[i][1])
    return pwys

def j_mod(pwy1, pwy2):
    return 1.0 - double(inner(pwy1[1],pwy2[1])) / double(min(sum(pwy1[1]),sum(pwy2[1]))) * double(max(sum(pwy1[1]),sum(pwy2[1]))) / double((sum(pwy1[1]+pwy2[1]) - inner(pwy1[1],pwy2[1])))


def nullDistGen(pwys,basis):
    nullD = []
    for i in pwys:
        new_pwy = [1]*sum(i.gvect) + [0]*(len(basis) - sum(i.gvect))
        shuffle(new_pwy)
        nullD.append(Path(i.name, new_pwy))
    return nullD

def clustScatter(clusters):
    W = 0
    for i in clusters:
        for x in range(len(i)):
            for y in range(len(i)):
                if x < y:
                    W += i[x].jac(i[y])/len(i)
    return W

def gapVal(n, clusters, pwys, basis):
    null_repeats = 15
    W_b = [0]*null_repeats
    for i in range(null_repeats):
        W_b[i] = clustScatter(bestClustering(nullDistGen(pwys, basis),n))
    W_null = sum(map(lambda x: math.log(x), W_b))/null_repeats
    W_std = math.sqrt(sum(map(lambda x: math.pow((math.log(x) - W_null),2),W_b)))
    return [W_null-math.log(clustScatter(clusters)), W_std]

def gapSet(min_k,max_k, pwys, basis):
    gap_k = []
    std_k = []
    for i in range(min_k,max_k): # max_k + 1 ?
        clusters = bestClustering(pwys, i)
        gap_stat = gapVal(i, clusters, pwys, basis)
        gap_k.append(gap_stat[0])
        std_k.append(gap_stat[1])
    return [gap_k, std_k]
    
def bestClustering(pwys, n):
    n_iter = 15
    cluster_c = [0]*n_iter
    cluster_e = [0]*n_iter
    for i in range(n_iter):
        #print
        #print
        #print
        #print
        cluster_c[i] = KMeans(pwys,n)
        cluster_e[i] = clustScatter(cluster_c[i])
    return cluster_c[cluster_e.index(min(cluster_e))]

def printC(clusters):
    for i in clusters:
        print
        for j in i:
            print j

def printC_size(clusters):
    for i in clusters:
        print len(i)
                
def KMeans(pwys, n):
    # takes in pathway list and number of clusters
    # potentially take in distance metric as argument
    new_centroids = [Path('',[0 for i in range(len(pwys[0].gvect))]) for j in range(n)]
    new_clusters = [[] for j in range(n)]

    centroids = []
    equals = False
    iter = 0
    while not equals and iter < 10: 
        #print 'Clustering'
        iter+=1
        if centroids != []:
            centroids = new_centroids
            clusters = new_clusters
            new_centroids = [Path('',[0 for i in range(len(pwys[0].gvect))]) for j in range(n)]
            new_clusters = [[] for j in range(n)]
        
        else:
            centroids = sample(pwys,n)
        for i in pwys:
            min_d = 1
            index = -Inf
            for j in centroids:
                min_d0 = min_d
                min_d = min(min_d0, i.jac(j))
                if min_d < min_d0:
                    index = centroids.index(j)
            if index == -Inf:
                new_clusters[sample(range(n),1)[0]].append(i)
            else:
                new_clusters[index].append(i)
        #printC_size(new_clusters)
        for i in new_clusters:
            #print len(i)
            for j in i:
                c_name = 'C' + str(new_clusters.index(i))
                new_centroids[new_clusters.index(i)] = Path(c_name, map(lambda x,y: x + y, new_centroids[new_clusters.index(i)].gvect, j.gvect))
            new_centroids[new_clusters.index(i)].gvect =  map(lambda x: double(x) / len(i), new_centroids[new_clusters.index(i)].gvect)
            #print new_centroids[new_clusters.index(i)].gvect
        equals = True
        for i in centroids:
            if not i.gvect == new_centroids[centroids.index(i)].gvect:
                equals = False
    return clusters
            


    
                    
            
            
            
    
        

basis = getBasis(pwys)
pwys2 = sendtoClass(genetoNum(pwys, basis))
#pwys3 = nullDistGen(pwys2, basis)
#clust_test = KMeans(pwys2, 20)
#clust_best = bestClustering(pwys2, 20)
gappy = gapSet(20,70,pwys2,basis)





#### null distribution testing
##counter = 0
##for i in range(len(pwys2)):
##    if len(pwys2[i][1]) != len(pwys3[i][1]):
##        print 'UH OH!'
##    if inner(pwys2[i][1],pwys3[i][1]) == sum(pwys2[i][1]):
##        print 'UH Oh!'
##        counter+=1

#### j_mod test, cutoff ~= .35
##jm = []
##for i in range(len(pwys2)):
##    for j in range(len(pwys2)):
##        if i < j:
##            jm.append(pwys2[i].jac(pwys2[j]))
##            if pwys2[i].jac(pwys2[j]) == 0:
##                print pwys2[i]
##                print pwys2[j]
##                print pwys2[i].jac(pwys2[j])
##                print

               
