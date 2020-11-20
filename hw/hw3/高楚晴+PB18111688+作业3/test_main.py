import unittest

from main import Student, Student2, MyDict


class TestHW3(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("student")
        self.student2 = Student2("student2", 3.14)
        self.my_dict1 = MyDict({'a': 1, 'b': 0, 'c': 2})
        self.my_dict2 = MyDict({'a': 2, 'b': 0, 'd': 1})
        self.my_dict3 = MyDict({})

    def test_student_init(self):
        assert self.student.name == 'student'

    def test_change_name_failed(self):
        self.student.name = ''
        self.student.name = '-stu'
        self.student.name = 'hello-world'
        self.student.name = '\nstudent'
        self.student.name = 'stud'
        self.student.name = 'studentname'
        assert self.student.name == "student"

    def test_change_name_success(self):
        valid_names = ['hello123', '12345', '123World', 'HelloWorld', ]
        for name in valid_names:
            self.student.name = name
            assert self.student.name == name

    def test_student2_init(self):
        for name, score in zip(['', 'hello', 'world'], [0, -100, 1.2]):
            student2 = Student2(name, score)
            assert student2.name == name
            assert student2.score == score

    def test_student2_read_only(self):
        with self.assertRaises(AttributeError):
            self.student2.name = 'new_name'
        with self.assertRaises(AttributeError):
            self.student2.score = 2
        with self.assertRaises(AttributeError):
            del self.student2.name
        with self.assertRaises(AttributeError):
            del self.student2.score

    def test_my_dict_add(self):
        assert self.my_dict1 + self.my_dict2 == {'a': 3, 'b': 0} == self.my_dict2 + self.my_dict1
        assert self.my_dict1 + self.my_dict3 == {} == self.my_dict3 + self.my_dict2

    def test_my_dict_sub(self):
        assert self.my_dict1 - self.my_dict2 == {'a': -1, 'b': 0}
        assert self.my_dict2 - self.my_dict1 == {'a': 1, 'b': 0}
        assert self.my_dict1 - self.my_dict3 == {} == self.my_dict3 - self.my_dict2

    def test_my_dict_mul(self):
        assert self.my_dict1 * self.my_dict2 == {'a': 2, 'b': 0} == self.my_dict2 * self.my_dict1
        assert self.my_dict1 * self.my_dict3 == {} == self.my_dict3 * self.my_dict2

    def test_my_dict_div(self):
        assert self.my_dict1 / self.my_dict2 == {'a': 0.5, 'b': 'NA'}
        assert self.my_dict2 / self.my_dict1 == {'a': 2, 'b': 'NA'}
        assert self.my_dict1 / self.my_dict3 == {} == self.my_dict3 / self.my_dict2


if __name__ == "__main__":
    unittest.main()
