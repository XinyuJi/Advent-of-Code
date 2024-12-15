with open('14.txt', 'r') as file:
    data = file.readlines()

width, height = 101, 103

def robots_data_praser(data):
    robots = []
    for line in data:
        if line.strip() == "":
            continue
        p,v = line.split()
        px,py = map(int,p[2:].split(",")) 
        vx,vy = map(int,v[2:].split(","))
        robots.append(((px,py),(vx,vy)))
    return robots

robots = robots_data_praser(data)
seconds = 0
while True:
    grid = [[0 for _ in range(width)] for _ in range(height)]
    seconds += 1
    collision = False
    for robot in robots:
        (px,py), (vx,vy)= robot
        nx,ny = px + seconds*vx, py + seconds*vy
        nx, ny = nx%width, ny%height
        grid[ny][nx] += 1
        if grid[ny][nx] > 1:
            collision = True
    
    if not collision:
        print(seconds)
        for row in grid:
            print("".join(map(str,row)))
        break
