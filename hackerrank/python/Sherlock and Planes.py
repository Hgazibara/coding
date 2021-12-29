def read_points():
    
    points = []
    
    for case in range(4):
        points.append([int(x) for x in input().strip().split()])
        
    return points


def vector_diff(p1, p2):
    return [x-y for x,y in zip(p2, p1)]


def cross_product(p1, p2):
    return [p1[1]*p2[2]-p1[2]*p2[1], p1[0]*p2[2]-p1[2]*p2[0], p1[0]*p2[1]-p1[1]*p2[0]]


def dot_product(v1, v2):
    return sum([x*y for x,y in zip(v1, v2)])


def get_surface_normal(p1, p2, p3):
    
    v1 = vector_diff(p1, p2)
    v2 = vector_diff(p1, p3)
    
    return cross_product(v1, v2)


def get_plane_const(normal, point):
    return -1*dot_product(normal, point)


def is_point_in_plane(normal, const, point):
    return (dot_product(normal, point) + const) == 0
    

for t in range(int(input())):
    p1, p2, p3, p4 = read_points()
    normal = get_surface_normal(p1, p2, p3)
    const = get_plane_const(normal, p1)
    print('YES' if is_point_in_plane(normal, const, p4) else 'NO')