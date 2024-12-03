def get_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()

    lines = data.splitlines()
    rows = [tuple(map(int, line.split())) for line in lines]
    return rows
