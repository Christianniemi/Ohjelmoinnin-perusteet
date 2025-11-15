from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    """
    Add a square to the drawing.
    """
    PDwg.add(Rect(insert=(int(left), int(top)),
                  size=(int(sideLength), int(sideLength)),
                  fill=color,
                  stroke=strokeColor))
    return None

def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    """
    Add a circle to the drawing.
    """
    PDwg.add(Circle(center=(int(centerX), int(centerY)),
                    r=int(radius),
                    fill=color,
                    stroke=stroke))
    return None

def saveSvg(PDwg: Drawing, file: str) -> None:
    """
    Save the drawing to an SVG file.
    """
    print(f'Saving file to "{file}"')
    proceed = input("Proceed (y/n)?: ").lower()
    if proceed == "y":
        PDwg.saveas(file, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")
    return None
