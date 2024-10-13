import math

type Coordinates = tuple[float, float]
type Point = tuple[str, Coordinates]

def get_point_label(a: Point) -> str:
    return a[0]

def get_point_x(a: Point) -> float:
    return a[1][0]

def get_point_y(a: Point) -> float:
    return a[1][1]

def get_farthest_point(m: Point, points: list[Point]) -> Point:
    if len(points) == 0:
        raise RangeError("There needs to be at least one point to calculate")
    elif len(points) == 1:
        return points[0]

    sorter = lambda point: (get_point_x(point) - get_point_x(m)) ** 2 + (get_point_y(point) - get_point_y(m)) ** 2
    points_by_distance = sorted(points, key = sorter, reverse = True)
    return points_by_distance[0]

def main():
    print("Let's detect the farthest point to a given point.")

    try:
        print("Point M (x, y) is a point to calculate distance to.")
        x = float(input('Input x: '))
        y = float(input('Input y: '))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    m: Point = ["M", [x, y]]
    print(f"Defined point: {m}")
    print("Now let's define some points to check.")

    points: list[Point] = []
    while True:
        label = input('Input point label (empty to end): ')
        if not label:
            if len(points) == 0:
                print("No points entered. Exiting program.")
                return
            else:
                break
        elif label == "M" or label in map(get_point_label, points):
            print(f"Point with label {label} already exists! Try again")
            continue

        try:
            x = float(input('Input x: '))
            y = float(input('Input y: '))
            points.append([label, [x, y]])
        except ValueError as e:
            print(f"Invalid input: {e}")

    print(f"Defined list of points: {points}")
    print(f"Farthest point is {get_point_label(get_farthest_point(m, points))}")

if __name__ == "__main__":
    main()