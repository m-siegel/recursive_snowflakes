"""
    I-M Siegel
    11/5/21

    Draws two types of snowflakes: one built off of triangles and one
    made of branching lines.
"""

import turtle
import triangle_flake
import branching_flake


def draw_triangle_flake():
    """
        Draw triangle snowflake in lower right of screen; return to center.
    """

    # Move away from center to give triangle flake room
    turtle.penup()
    turtle.right(30)
    turtle.forward(60)

    # Set pencolor
    turtle.pendown()
    turtle.pencolor(255, 255, 255)

    # Draw triangle snowflake
    triangle_flake.snowflake(240, 4)

    # Return to center
    turtle.penup()
    turtle.backward(60)
    turtle.left(30)


def draw_branching_flake():
    """
        Draw branching snowflake in upper left of screen; return to center.
    """

    # Move away from center to give branching flake room
    turtle.right(45)
    turtle.backward(200)
    turtle.left(45)

    # Reset pen color
    turtle.pendown()
    turtle.pencolor(16, 27, 255)

    # Draw branching snowflake
    branching_flake.branch_flake(180, 3, 6)

    # Return to center
    turtle.penup()
    turtle.right(45)
    turtle.forward(200)
    turtle.left(45)


def main():
    """
        Draws two types of snowflakes: one built off of triangles and one
        made of branching lines. Both are drawn recursively.
    """

    # Set background color
    turtle.colormode(255)
    turtle.bgcolor(160, 140, 255)

    # Draw triangles, returning to center after each
    draw_triangle_flake()
    draw_branching_flake()


if __name__ == "__main__":
    main()
