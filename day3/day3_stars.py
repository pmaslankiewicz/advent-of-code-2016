def read_file():
    with open('input3.txt') as f:
        triangle_list = []
        for line in f:
            vertices = line.strip().split()
            triangle_list.append(vertices)
        return triangle_list

def is_valid(vertices):
    vertices.sort()
    return int(vertices[2]) < int(vertices[1]) + int(vertices[0])

def transform_triangle_list(triangle_list):
    new_triangle_list = []
    for i in range(0, len(triangle_list), 3):
        for j in range(3):
            new_triangle_list.append([triangle_list[i][j], triangle_list[i+1][j], triangle_list[i+2][j]])
    return new_triangle_list

def main():
    triangle_list = transform_triangle_list(read_file())
    valid_count = 0
    for triangle in triangle_list:
        num_triangle = [int(vertex) for vertex in triangle]
        if is_valid(num_triangle):
            valid_count += 1
    print "valid count: %d" % valid_count

main()