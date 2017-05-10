x, y, z, = 1, 1, 1
n = 2

#print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n])

coord=[]
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a + b + c != n:
                coord.append([a, b, c])
print(coord)