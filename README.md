# diffshapes_turtle
Turtle drawing different shapes jsut chan ge the value of n
The provided code seems to be drawing multiple shapes using the turtle library. Here's a breakdown of the functionality and some improvements:

Code Breakdown:

Imports:

turtle: Imports the turtle library for drawing shapes.
Turtle and Screen from turtle: Imports specific classes from the library.
Setting Up:

tim = Turtle(): Creates a turtle object named tim for drawing.
screen = Screen(): Creates a screen to display the drawings.
Turtle Customization (commented out):

tim.shape("turtle"): Sets the turtle's shape to a turtle (commented out).
tim.color("red"): Sets the turtle's color to red (commented out).
Drawing Shapes (commented out):
These commented sections demonstrate how to draw a square and circles using forward, right, and left commands.

Star Drawing (commented out):
This section (commented out) likely draws a star using a loop and combinations of forward and right commands.

Current Functionality:

The uncommented loop iterates from 3 to 8 (inclusive).
Inside the inner loop (j loop):
tim.forward(80): Moves the turtle forward 80 units.
tim.right(360.0 / i): Turns the turtle right by a calculated angle based on the outer loop variable i. This creates shapes with varying side numbers.
Screen Management (commented out):

tim.color("blue") (commented out): Sets the turtle's color to blue (commented out).
tim.forward(40) and tim.right(theta) (commented out): Likely intended to draw additional shapes with a specific angle theta (commented out).
Screen Exit:

screen.exitonclick(): Keeps the screen open until the user clicks to close it.





Output for n==9 
ie 9 images
![image](https://github.com/guptuv/diffshapes_turtle/assets/116263507/95cc3142-9ba2-461e-a474-1a666fe5c5e8)



Output for n=9 but turn.left() is used 
![image](https://github.com/guptuv/diffshapes_turtle/assets/116263507/bebf1b4f-ab74-49df-8ab2-eb47a400b0ac)

