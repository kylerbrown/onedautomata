'''A simple program for generating 1d cellular automata'''
from numpy import array, arange, flipud, mod, sum, zeros
import matplotlib.pyplot as plt

def num_to_binary_list(n):
    l = []
    for i in range(0,2**3):
        l.append(n % 2)
        n /= 2

    l.reverse()
    return array(l)
   
def update_cell(l,rule):
    '''l is a list of neighbor cells'''
    return flipud(rule)[sum(flipud(2**arange(0,3))*l)]
    
def update_row(p,rule):
    '''p is previous row'''
    r = zeros(p.size)
    for i in arange(p.size):
        neighbors = p[mod(array([i-1, i, i+1]),p.size)]
        r[i]=update_cell(neighbors, rule)
        
    return r

def n_updates(rule,X,Y):
    '''create a matrix of size sidel x sidel using RULE'''
    M = zeros([Y,X])
    M[0,M.shape[1]/2]=1 #seed first row
    for i in arange(1,M.shape[0]):
        M[i,:]=update_row(M[i-1,:], rule)

    return M

if __name__ == '__main__':
    dec_rule=30
    rule = num_to_binary_list(dec_rule)
    X = 100
    Y = 50
    m = n_updates(rule,X,Y)
    fig = plt.figure(figsize=(36*2,24*2),dpi=600)
    plt.imshow(m,cmap='Greys',interpolation='nearest')
    #plt.pcolor(flipud(m), cmap='Greys')
    plt.axis('off')
    plt.savefig("rule_"+repr(dec_rule)+"_size_"+repr(Y)+"_imshow.png", bbox_inches='tight')
    #plt.savefig("rule_"+repr(dec_rule)+"_size_"+repr(sidel)+".pdf",
    # bbox_inches='tight')    
    #plt.show()
    


        
