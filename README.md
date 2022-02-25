# geometrycalcs

program that calculates area and perimeter of geometry objects
Implemented entirely with object oriented programming

Four classes are created: Polygon, Triangle, Rectangle, Square

The Triangle and Rectangle class are subclasses of Polygon. Square is ia subclass of Rectagle.

The Polygon class raises a NotImplementedError when the get_area() and get_sides() methods are called. However, it correctly returns the perimeter
of the polygon when get_perimeter() is called. The Polygon class is treated as abstract class.

Triangle class has a constructor that takes in 3 arguments, which will be the lenghts of the 3 sides of the triangle. It is assumed that sides passed
to the constructor will always form a valid triangle.

The Rectangle class has a constructor that takes in 2 arguments, which are the width and height of the Rectangle.

The Square class has a constructor that takes in 1 argument, which is the length of the side.

Triangle and Rectangle classes both have implemented the following methods:

get_sides(): Returns a list containing the lengths of the sides of the shape.

get_area(): returns the area of the polygon.

The Square class only has an implementation for its constructor, and relies on the Rectangle superclass for implementations of get_sides() and get_area().

Example of how the program behaves:

=> triangle = Triangle(2, 5, 6)

=>  triangle.get_area()

4.68

=> Square(4).get_perimeter()

16

=> Rectangle(3, 5).get_sides()

[3, 5, 3, 5]
