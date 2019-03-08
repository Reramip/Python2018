##Calculate distance between two points.
import point

def main():
    x1 = eval(input("Enter x-cooradinate of first point: "))
    y1 = eval(input("Enter y-cooradinate of first point: "))
    x2 = eval(input("Enter x-cooradinate of second point: "))
    y2 = eval(input("Enter y-cooradinate of second point: "))
    x = x2 - x1
    y = y2 - y1
    poi = point.Point(x, y)
    print("Distance between points: {0:.2f}".format(poi.distanceFromOrigin()))

main()