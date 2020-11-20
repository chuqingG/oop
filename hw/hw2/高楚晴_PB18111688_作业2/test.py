import random
import unittest

from main import sum_of_all, Shape, Circle, Square

PI = 3.1415926


class MyFloat(float):
    def __eq__(self, other) -> bool:
        return abs(self - other) < 1e-8


class TestHW2(unittest.TestCase):
    def setUp(self) -> None:
        self.shape = Shape()
        self.diameter = random.random() * 10
        self.side = random.random() * 10
        self.circle = Circle(self.diameter)
        self.square = Square(self.side)

    def test_sum_of_all(self):
        assert sum_of_all(1, 2, 3, 4, 5) == 15
        assert sum_of_all(1, 2, 3, 4, 5, block=2) == 19
        assert sum_of_all(1, 2, 3, 4, inverse=True) == MyFloat(25 / 12)
        assert sum_of_all(1, 2, 3, 4, block=2, inverse=True) == MyFloat(7 / 12)

    def test_sub_class(self):
        # Circle和Square均需继承父类Shape
        assert issubclass(Circle, Shape)
        assert issubclass(Square, Shape)

    def test_area(self):
        assert self.circle.get_area() == MyFloat(PI * (self.diameter / 2) ** 2)
        assert self.square.get_area() == MyFloat(self.side ** 2)

    def test_attribute(self):
        assert hasattr(self.circle, 'diameter')
        assert not hasattr(self.circle, 'side')

        assert not hasattr(self.square, 'diameter')
        assert hasattr(self.square, 'side')

        assert not hasattr(self.shape, 'diameter')
        assert not hasattr(self.shape, 'side')
        assert hasattr(self.shape, 'name')
        assert hasattr(self.shape, 'area')

    def test_default(self):
        # 默认为单位圆和单位正方形
        assert Circle().get_area() == MyFloat(PI)
        assert Square().get_area() == MyFloat(1.)

    def test_no_overwrite(self):
        # 不能重写Circle和Square类中的get_area方法
        assert Circle.get_area == Square.get_area == Shape.get_area


if __name__ == "__main__":
    random.seed(0)
    unittest.main()
