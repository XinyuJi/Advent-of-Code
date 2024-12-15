with open('14.txt', 'r') as file:
    data = file.readlines()

width, height = 101, 103
matrix = [0,0,0,0]

for line in data:
    if line.strip() == "":
        continue
    p,v = line.split()
    px,py = map(int,p[2:].split(",")) 
    vx,vy = map(int,v[2:].split(","))
    nx,ny = px + 100*vx, py + 100*vy
    nx,ny = nx % width, ny % height

    mid_x, mid_y = width//2, height//2
    if nx == mid_x or ny == mid_y:
        continue
    if nx < mid_x and ny < mid_y:
        matrix[0] += 1
    elif nx > mid_x and ny < mid_y:
        matrix[1] += 1
    elif nx < mid_x and ny > mid_y:
        matrix[2] += 1
    else:
        matrix[3] += 1

safety_factor = matrix[0] * matrix[1] * matrix[2] * matrix[3]
print(safety_factor)
