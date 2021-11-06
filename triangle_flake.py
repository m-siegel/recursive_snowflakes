"""
    I-M Siegel
    11/5/21

    Draws a snowflake, like a triangle or hexagon where each line segment is
    replaced by -^-, recursively, until the remaining line segments are very
    small.
"""


import turtle


def snowflake(length, depth):
    """
        Draws a snowflake as a triangle, each of whose sides is a drawn by
        fractal_edge, which recursively replaces a line --- with
        the shape -^-.
        Param: length: Length of the largest 'side' of the triangle.
    """

    # Draw triangle where each side is a fractal -^-
    for i in range(3):
        fractal_edge(length, depth)
        turtle.right(120)


def fractal_edge(length, depth):
    """
        If length less than 9, draws line of length length from starting
        point in starting direction.
        Otherwise, draws -^- instead of a line ---, ending up in the
        same position as it would have if it had just drawn a line.
        Param: length: Length of line between starting point and ending point.
    """

    # Base case: draw straight line at deepest level of recursion
    if depth <= 0:
        turtle.forward(length)

    # Otherwise, recursively replace each straight line --- with -^-
    else:

        # Length of each segment traveled in __ / \ __
        segment = length / 3

        # Draw first segment __
        fractal_edge(segment, depth - 1)

        # Draw uphill /
        turtle.left(60)
        fractal_edge(segment, depth - 1)

        # Draw downhill \
        turtle.right(120)
        fractal_edge(segment, depth - 1)

        # Draw ending flat segment __
        turtle.left(60)
        fractal_edge(segment, depth - 1)


def main():
    snowflake(243, 4)


if __name__ == "__main__":
    main()
