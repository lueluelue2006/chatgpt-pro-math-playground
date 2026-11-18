"""Verify an integer 315-by-315 Mondrian tiling with area range 150."""


SIDE = 315
# Each row gives the lower-left corner, width, and height.
RECTANGLES = (
    (0, 0, 90, 157),
    (0, 157, 90, 158),
    (90, 0, 112, 126),
    (202, 0, 113, 126),
    (90, 126, 75, 189),
    (165, 126, 150, 94),
    (165, 220, 150, 95),
)


def verify():
    coverage = bytearray(SIDE * SIDE)
    shapes = set()
    areas = []
    assert len(RECTANGLES) == 7
    for x, y, width, height in RECTANGLES:
        assert all(type(n) is int for n in (x, y, width, height))
        assert 0 <= x < x + width <= SIDE
        assert 0 <= y < y + height <= SIDE
        shape = tuple(sorted((width, height)))
        assert shape not in shapes
        shapes.add(shape)
        areas.append(width * height)
        for j in range(y, y + height):
            for i in range(x, x + width):
                coverage[j * SIDE + i] += 1

    assert all(count == 1 for count in coverage)
    assert sum(areas) == SIDE**2
    assert max(areas) - min(areas) == 150
    print(f"{len(shapes)} distinct shapes cover all {SIDE**2:,} unit cells exactly once.")
    print("Areas:", *areas)
    print(f"Area range: {max(areas)} - {min(areas)} = {max(areas) - min(areas)}")


if __name__ == "__main__":
    verify()
