"""
    I-M Siegel
    11/5/21

    Draws a branching snowflake, like a star made of lavender or wheat.
"""


import turtle


def main():
    branch_flake(180, 3, 6)


def branch_flake(length, depth, branches, joints=3, shrink_mitigator=1):
    """
        Draws a branching snowflqke, like a leave or tree from above.
        :param length: Length of longest branch
        :param depth: Depth of recursion
        :param branches: Number of main branches from the heart of the flake
        :param joints: Number of child branches per parent branch
        :param shrink_mitigator: (advanced) How much to slow shrinking of
                                 child branches farther from root of parent
    """
    # Angle between parent branch and child branch
    angle = 360 / (branches * 2)

    # Draw branches number of branches
    for i in range(branches):
        branch(length, depth, angle, joints, shrink_mitigator)
        turtle.right(2 * angle)


def branch(length, depth, angle, joints, shrink_mitigator):
    """
        Draws a line with pairs of child branches branching off of it
        recursively.
        :param length: Length of branch
        :param depth: Number of recursive calls to go before base case
        :param angle: Degrees between child branch and parent branch
        :param joints: Number of child branches per parent branch
        :param shrink_mitigator: (advanced) How much to slow shrinking of
                                 child branches farther from root of parent
    """

    # Base case, just draw a line and return to starting condition
    if depth == 0:
        turtle.forward(length)
        turtle.backward(length)

    # Recursive branching
    else:

        # Length of segments on branch between child branches
        segment = length / joints

        # Start i at 1 to use in shrinking factor for child branches
        for i in range(1, joints + 1):

            # Pairs of recursive branches shrink more further from base
            # of parent branch
            shrink_factor = 1 + (i / 5)
            shrunk_segment = shrink_mitigator * segment / shrink_factor

            # Draw main branch up to next joint
            turtle.forward(segment)

            # Left recursive branch
            turtle.left(angle)
            branch(shrunk_segment, depth - 1, angle, joints, shrink_mitigator)

            # Right recursive branch
            turtle.right(2 * angle)
            branch(shrunk_segment, depth - 1, angle, joints, shrink_mitigator)

            # Face forward again
            turtle.left(angle)

        # Return to base of main branch
        turtle.backward(length)


if __name__ == "__main__":
    main()
