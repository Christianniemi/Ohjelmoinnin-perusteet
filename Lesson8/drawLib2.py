import math
import svgwrite
from svgwrite.shapes import Rect, Circle
from svgwrite.shapes import Polygon

def drawSquare(PDwg: svgwrite.Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    PDwg.add(Rect(insert=(x, y),
                  size=(side, side),
                  fill=fill,
                  stroke=stroke))

def drawCircle(PDwg: svgwrite.Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center X coord: "))
    cy = int(input("- Center Y coord: "))
    r = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    PDwg.add(Circle(center=(cx, cy),
                    r=r,
                    fill=fill,
                    stroke=stroke))

def drawHexagon(PDwg: svgwrite.Drawing) -> None:
    print("Insert hexagon details:")
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = int(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    # circumradius R = apothem / cos(30°)
    R = apothem / math.cos(math.radians(30))

    # kulmat: aloitetaan top right (−30°) ja mennään myötäpäivään
    angles = [-30, 30, 90, 150, 210, 270]
    points = []
    for ang in angles:
        x = cx + R * math.cos(math.radians(ang))
        y = cy + R * math.sin(math.radians(ang))
        points.append((round(x), round(y)))

    PDwg.add(Polygon(points=points, fill=fill, stroke=stroke))

def saveSvg(PDwg: svgwrite.Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").lower()
    if proceed == "y":
        PDwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")
