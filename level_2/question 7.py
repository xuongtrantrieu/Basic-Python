def xy_dimension(n, m):
    xy = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            xy[i][j] = i * j

    return xy

if __name__ == '__main__':
    print(xy_dimension(3, 4))
