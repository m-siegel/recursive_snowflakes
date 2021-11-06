## About

I wrote these functions to practice recursion.

The programs are written in Python and use the turtle package.

### *triangle_flake*
Contains a function, *snowflake*, to draw a Koch snowflake (see fig. 1).

Caller determines
* the length of the side of the largest, foundational, triangle.
* the depth of recursion.


![figure 1: a Koch snowflake](/Images/fig_1_triangle_snowflake.jpg)
figure 1: a Koch snowflake. It is made up of triangular points. The number of
points is a multiple of 6.

### *branching_flake*
Contains a function, *branch_flake*, to draw a Koch snowflake (see fig. 2 and
fig. 3).

Caller determines
* the length of the largest branches that form the star.
* the number of large branches.
* the depth of recursion.

Caller *may* determine
* the number of pairs of child branches per parent branch.
* the factor by which child branches shrink as they get farther from the root 
of the parent branch.

![figure 2: a branching snowflake with twelve branches](/Images/fig_2_branching_snowflake_1.jpg)
figure 2: A branching snowflake with twelve main branches, four pairs of child
branches (joints) per parent branch, and four levels of recursion.

![figure 3: a branching snowflake with six branches](/Images/fig_3_branching_snowflake_2.jpg)
figure 3: A branching snowflake with six main branches, three joins per parent
branch, four levels of recursion, and relatively long child branches.

### *blizzard*
Blizzard draws one white Koch snowflake in the lower right of a purple canvas
and one dark blue branching snowflake in the upper left of the canvas (see
fig. 4).

![figure 4: result of running blizzard](/Images/fig_4_blizzard.jpg)
figure 4: The result of running blizzard.
