def solution(n, edges):
    edges.reverse()
    arr = []
    tree_list = []
    for i in edges:
        arr.append(i[1])
        arr.append(i[0])
        if i[0] != 0:
            arr = re_entry(edges,arr,i[0],edges.index(i))
        arr.reverse()
        tree_list.append(arr)
        arr = []
    print(tree_list)

def re_entry(edges,arr,i0,start):
    for j in edges[start+1:]:
        if i0 == j[1]:
            arr.append(j[0])
            if j[0] != 0:
                arr = re_entry(edges,arr,j[0],edges.index(j))
            return arr
