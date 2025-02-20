There are several files that you will need as they comprise the newton's model solver for the second part of Assignment 1.

The first file, contained in the src/newtonsmethod folder, is "solver_main", which contains the algorithm for newton's method. In the file, users will be asked to input:

Integer value for function type
Integer value for number of iterations
Numerical value for x_0.
The second file is "solver_functions", that the main file (solver_main) will run and which contains functions that the solver will call upon when it is run.

Example Run: On starting (running) the solver_main, after simply:

Inputting a integer value for which function the solver will use (can choose from functions 1, 2, 3, or 4, unforunately 5 is still being worked on)
Inputting an integer value for number of iterations
Inputting some value for x_0 (can be positive or negative, can be a decmical or a whole number)
The solver will put the value for x_0 through the chosen function's main and prime (derivative) form, before using them all as variables for the formula for newton's method: (x_n+1 = x_n + f(x)/f'(x))

It will run recursively for however many iterations the user has set to, and if that value is large enough eventually the user will notice that the final values for x_n and f(x) have settled on some consistently repeating value, which should be the convergence (a root) of the function. Depending on the direction it was approached (whether the input value for x_0 was positive or negative) the root may also be positive or negative, and may be only one of several roots for the function.
