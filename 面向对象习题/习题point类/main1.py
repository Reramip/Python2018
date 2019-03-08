##Calculate distance from origin to a point.
import point

def main():
    x = eval(input("Enter x-coordinate of point: "))
    y = eval(input("Enter y-coordinate of point: "))
    poi = point.Point(x, y)
    print("Distance from origin: {0:.2f}".format(poi.distanceFromOrigin()))

main()