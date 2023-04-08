import unittest

from descriptor.descriptor import MyClass


class DescriptorTest(unittest.TestCase):

    def test1_init_lower_name(self):
        # Test if when it is saved from the init it is saved in lowercase.
        name: str = 'MyName'
        my_class = MyClass(name)
        self.assertNotEqual(name, my_class.name)
        self.assertEqual(name.lower(), my_class.name)

    def test2_set_lower_name(self):
        # Test if when it is saved from the setter it is saved in lowercase.
        name: str = ''
        my_class = MyClass(name)
        self.assertEqual(name, my_class.name)
        name = 'MyName'
        my_class.name = name
        self.assertNotEqual(name, my_class.name)
        self.assertEqual(name.lower(), my_class.name)
