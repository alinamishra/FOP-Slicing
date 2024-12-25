# graph representation
​
adj_list ={
    "44":[],
    "45":["44"],
    "46":["45","2"],
    "47":["46","48"],
    "48":[],
    "2":["46"],
    "3":["2"],
    "4":["3"],
    "5":["4","2"],
    "6":["47","16"],
    "16":["31","6"],
    "31":["16"],
    "7":["6","4"],
    "8":["7","14"],
    "14":["6"],
    "32":["31","4"],
    "33":["32","4"],
    "34":["34"],
    "35":["33"],
    "36":["4"],
    "37":["36"],
    "38":["37"],
    "39":["38"],
    "40":["38"],
    "41":["40"],
    "42":["41","43"],
    "43":["31"],
    "17":["16","4"],
    "19":["17","4"],
    "20":["19"],
    "21":["20"],
    "22":["22"],
    "23":["20","24"],
    "24":["25"],
    "25":[],
    "26":["25"],
    "27":["25","29"],
    "29":["16"]
}
## required array and dictionary
color = {} # W, G, B
parent = {}
trav_time = {} # [start,end]
dfs_traversal_output = []
​
# initialize
number = int(input("Enter a node: "))
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]
    
time = 0
def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time +=1
    
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
            
    color[u] = "B"
    trav_time[u][1] = time
    time +=1
​
    
dfs_util("42")
print("DFS of the given node are")
print(dfs_traversal_output)
​
