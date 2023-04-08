import unittest

from adapter.adapter import NewLibrary, OldLibrary, Adapter


class AdapterTest(unittest.TestCase):

    def test1_add_method_get_description(self):
        # The adapter adds the method description
        library = NewLibrary()
        with self.assertRaises(AttributeError):
            library.get_description()
        library = Adapter()
        self.assertTrue(bool(library.get_description()))

    def test2_adapter_get_description(self):
        # The adapter returns the same as the old library.
        old_library = OldLibrary()
        adapter = Adapter()
        self.assertNotEqual(old_library.get_description(), adapter.description())
        self.assertEqual(old_library.get_description(), adapter.get_description())
