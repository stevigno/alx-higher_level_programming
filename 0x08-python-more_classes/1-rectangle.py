class Rectangle:
    """
    Defines class rectangle with private attribute width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize rectangles.
        """
        self._validate_and_set_width(width)
        self._validate_and_set_height(height)

    @property
    def width(self):
        """
        Getter returns width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter sets width if int >= 0.
        """
        self._validate_and_set_width(value)

    def _validate_and_set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter returns height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter sets height if int >= 0.
        """
        self._validate_and_set_height(value)

    def _validate_and_set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
