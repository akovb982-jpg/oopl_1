from shapes import Triangle, Rectangle, Trapeze, Parallelogram, Circle

SHAPES = {
    "Triangle": Triangle,
    "Rectangle": Rectangle,
    "Trapeze": Trapeze,
    "Parallelogram": Parallelogram,
    "Circle": Circle,
}
def read_shapes(filename):
    shapes = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.split()     
            if not parts:
                continue
            name = parts[0]              
            params = parts[1:]           
            if name not in SHAPES:
                continue
            try:
                shape = SHAPES[name](*params)
                shapes.append(shape)
            except Exception:
                continue
    return shapes
def process(filename):
    print(f"\nFile: {filename}")
    print("-" * 40)
    shapes = read_shapes(filename)
    if not shapes:
        print("No valid shapes found.")
        return
    max_area   = max(shapes, key=lambda s: s.area())
    max_perim  = max(shapes, key=lambda s: s.perimeter())
    print(f"Max area:      {max_area}  -->  {max_area.area():.2f}")
    print(f"Max perimeter: {max_perim}  -->  {max_perim.perimeter():.2f}")
if __name__ == "__main__":
    for fname in ["input01.txt", "input02.txt", "input03.txt"]:
        process(fname)