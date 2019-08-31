"""
PROJECT TOPIC:Robust Location Detection in Emergency Sensor Networks
TEAM MEMBERS:
Andrew Boateng            1207412982 
Daya Kulkarni             1210843657
Moumita Laskar            1204363181
Rohith Kumar Punithavel   1215339827

INPUT: 1. Text file nodes.txt which gives the connection between the nodes.
       2. Enter the Sequence, when prompted, to traverse the graph
       
OUTPUT: Identifying Code.
"""

import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#Global Variables
#adjacency table and vertex_list are global
adj_table = []
vertex_list = []


  
#FUNCTION: create_graph()
#INPUT:    NONE
#OUTPUT:   GRAPH
#Des:      creates a graph by adding nodes and edges, inclusing itself
def create_graph():
    g = nx.read_edgelist('nodes.txt',nodetype=int,edgetype =int,create_using=nx.Graph())
   
    #add self reference
    for i in g.nodes():
        g.add_edge(i,i)
    return g


#FUNCTION: create_adjacency_table(graph,no_of_nodes)
#INPUT:    Graph
#          numberOfNodes in the graph
#OUTPUT:   adjacency Table
#Des:      creates a table of adjacent nodes(including itself) of a graph

def create_adjacency_table(graph,no_of_nodes):
    
    # NOTE: if i don't start with 1 in for loop
    #i get this error "networkx.exception.NetworkXError: The node 0 is not in the graph"
    #workaround is start from 1 and go till len+1, so that we get all the seven nodes
    for i in range(1,no_of_nodes+1):
        adj_table.append((list(graph.neighbors(i))))
    return adj_table


#FUNCTION: create_idList(D_list,no_of_nodes)
#INPUT:    D_List: C_list - {input_list[x]}
#          no_of_nodes: numberOfNodes in the graph
#OUTPUT:   id_list
#Des:      creates a table of Identifying code of each nodes for particular D_List

def create_idList(D_list,no_of_nodes):
    id_list = []
    for i in range(no_of_nodes):
        id_list.append(list(set(adj_table[i]) & set(D_list)))
    #print("id_list:  ",id_list)
    return id_list


#FUNCTION: create_idList(D_list,no_of_nodes)
#INPUT:    D_List: C_list - {input_list[x]}
#          no_of_nodes: numberOfNodes in the graph
#OUTPUT:   id_list
#Des:      creates a table of Identifying code of each nodes for particular D_List

def find_identifyingCode(id_list,no_of_nodes):
    for i in range(no_of_nodes):
        a = id_list[i]
        for j in range(i+1,no_of_nodes):
            if set(a) == set(id_list[j]):
                return 0
    return 1

#FUNCTION: find_idCode(C_list, input_list,no_of_nodes)
#INPUT:    C_list
#          input_list: sequence of visited nodes
#          no_of_nodes: numberOfNodes in the graph
#OUTPUT:   C_list: irrducible identifying codes
#Des:      creates an Identifying code for the graph

def find_idCode(C_list, input_list,no_of_nodes):
    for x in range(no_of_nodes):
        D_list = C_list.copy()
        D_list.remove(input_list[x])
        id_list = create_idList(D_list,no_of_nodes)

        #check for identifying code
        res = find_identifyingCode(id_list,no_of_nodes)
        if res == 1:
            C_list = D_list
    return C_list

        
#FUNCTION: id_code(input_list,no_of_nodes)
#INPUT:    input_list: sequence of visited nodes
#          no_of_nodes: numberOfNodes in the graph
#OUTPUT:   id_code: irrducible identifying codes
#Des:      creates an Identifying code for the graph

def id_code(input_list,no_of_nodes):
    C_list = vertex_list.copy()
    
    #check if the adjacency table we created is itself an unique or not
    #if we find that if the adj_table has atleast two nodes which has same list,
    #then we can't reduce the nodes any further and the list is  an unquie code.
    #id_C_Code = 0 => we found atleast two nodes in adj_table which are not unique
    # and we quit, else we proceed to get the reduced code.
    is_C_idcode = find_identifyingCode(adj_table,no_of_nodes)
    
    if is_C_idcode == 0:
        print("C itself is an identifying code")
        print("Cannot proceed further, GOODBYE")
        quit()
    C_list = vertex_list.copy()
    id_code = find_idCode(C_list,input_list,no_of_nodes)
    return id_code


#FUNCTION: draw_graph(graph,id_code)
#INPUT:    graph
#          id_code
#OUTPUT:   NONE
#Des:      plot the graph with id codes as red and other nodes as green
def draw_graph(graph,id_code):
    graph_nodes = list(graph.nodes())
    color_list = []
    
    for i in range(len(graph_nodes)):
        flag = 0
        for j in range(len(id_code)):
            if graph_nodes[i] == id_code[j]:
                flag = 1
                color_list.append('red')     
        if flag == 0:
            color_list.append('green')   
    nx.draw(graph, node_color=color_list,with_labels=True,font_color='white')
    plt.draw()
    plt.show()
    
if __name__ == "__main__":
    #create the graph
    graph = create_graph()
    
    #create adjacency list B(v)
    #adjacency list is a global variable
    no_of_nodes = graph.number_of_nodes()
    adj_table = create_adjacency_table(graph,no_of_nodes)
    #print("adj_table: ",adj_table)

    #create a vertex list
    vertex_list = list(graph.nodes())
    #print("vertex: ",vertex_list)

    #Read the input from user
    while(1):
        print("Total number of nodes in the graph is ",no_of_nodes)
        print("Please enter the input sequence which has ",no_of_nodes," number of nodes")
    
        input_list = []
        input_list = input()
        input_list = list(map(int, input_list.split()))
        if (len(input_list) == 0) or (len(input_list) != no_of_nodes):
            print("Please enter a valid input")
        else:
            break

    #function ID_CODE
    id_code = id_code(input_list,no_of_nodes)
    print("id_code:  ",id_code)


    #draw graph
    draw_graph(graph,id_code)
    
  

    
    
