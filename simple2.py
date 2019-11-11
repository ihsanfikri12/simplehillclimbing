graph = {'A': {'B':8,'D':7,'C':3},
         'B': {'A':8,'C':5,'D':4},
         'C': {'B':5,'D':6,'A':3},
         'D': {'A':7,'B':4,'C':6},
        }

induk = input("Masukan induk kota = ")
induk = induk.upper()
tambah = graph[induk[0]][induk[1]] + graph[induk[1]][induk[2]] + graph[induk[2]][induk[3]]


def short_graph (graph,induk,hitung,path = [], pathHitung = {}) :
    while True:
        path = []
        pathHitung = {}
        z = 0
        # print(hitung)
        for i in range(6):
            # print(induk)
            if i<len(induk)-1:
                a = induk[z]
                b = induk[z+1].lower()
                c = induk.replace(a,b)
                c = c.replace(b.upper(),a)
                path.append(c.upper())
                z +=1    
            elif i==4:
                z=3
                for y in range(2):
                    a = induk[z]
                    b = induk[y].lower()
                    c = induk.replace(a,b)
                    c = c.replace(b.upper(),a)
                    path.append(c.upper())
            elif i>=4:
                z=2
                a = induk[z]
                b = induk[0].lower()    
                c = induk.replace(a,b)
                c = c.replace(b.upper(),a)
                path.append(c.upper())
        
        for var in path:
            tambah = 0
            for i in range(len(var)-1):
                tambah =  tambah + graph[var[i]][var[i+1]]
                pathHitung [var] = tambah
            
        tambah = 0
       
        for var in pathHitung.keys():
            if (hitung<pathHitung[var]):
                tambah +=1
                print(pathHitung)
                if tambah==6:
                    return induk
                continue
            elif (hitung>pathHitung[var]):
                hitung = pathHitung[var]
                induk = var
                break
        # return None
print(short_graph(graph,induk,tambah))
