#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        # Initialize the width and height attributes with the provided values
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the Rectangle.

        Returns:
            int: The current width of the Rectangle.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        # Validate that the provided value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Validate that the provided value is non-negative
        if value < 0:
            raise ValueError("width must be >= 0")

        # Update the width attribute with the validated value
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle.

        Returns:
            int: The current height of the Rectangle.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        # Validate that the provided value is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        # Validate that the provided value is non-negative
        if value < 0:
            raise ValueError("height must be >= 0")

        # Update the height attribute with the validated value
        self.__height = value

    def area(self):
        """Calculate and return the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the Rectangle using the '#' character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for _ in range(self.__height):
            rect.extend(['#'] * self.__width)
            if _ != self.__height - 1:
                rect.append('\n')

        return ''.join(rect)

    def __repr__(self):
        """Return the official string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

