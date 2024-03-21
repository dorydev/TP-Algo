#------------------------------#
#
#
#       Spiral matrix
#          Algorithm
#
#
#------------------------------#


up, dwn, lft, rght = (0, -1), (0, 1), (-1, 0), (1, 0)
moov = {up: rght, rght: dwn, dwn: lft, lft:up}

def init_spiral_matrix(wdth, hght):

    if wdth < 1 or hght < 1:
        return -1
    x, y = wdth // 2, hght // 2 
    dx, dy = up 
    matrix = [[None] * wdth for _ in range(hght)]
    count = 0

    while True:
        count += 1
        matrix[y][x] = count 
        
        new_dx, new_dy = moov[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy

        if (0 <= new_x < wdth and 0 <= new_y < hght and matrix[new_y][new_x] is None):
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:
            x, y = x + dx, y + dy
            if not (0 <= x < wdth and 0 <= y < hght):
                return matrix 



def spiral_matrix_diagonal(matrix):
    l =  len(matrix[0])
    return [matrix[i][i] for i in range(1)]



res = spiral_matrix_diagonal(init_spiral_matrix(7, 7))
print(res)
    