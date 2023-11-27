#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__class__.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or sets the width of the Rectangle.

        Returns:
            int: The current width of the Rectangle.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        # Validates that the provided value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Validates that the provided value is non-negative
        if value < 0:
            raise ValueError("width must be >= 0")

        # Updates the width attribute with the validated value
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the Rectangle.

        Returns:
            int: The current height of the Rectangle.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        # Validates that the provided value is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        # Validates that the provided value is non-negative
        if value < 0:
            raise ValueError("height must be >= 0")

        # Updates the height attribute with the validated value
        self.__height = value

    def area(self):
        """Calculates and returns the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the Rectangle using the '#' character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for _ in range(self.__height):
            rect.extend(['#'] * self.__width)
            if _ != self.__height - 1:
                rect.append('\n')

        return ''.join(rect)

    def __repr__(self):
        """Returns the official string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Prints a message for every deletion of a Rectangle."""
        self.__class__.number_of_instances -= 1
        print("Goodbye, rectangle...")

