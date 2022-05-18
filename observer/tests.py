import unittest
from io import StringIO
from unittest.mock import patch
from observer.observer import DigitalMagazine, Subscriber


class ObserverTest(unittest.TestCase):

    def setUp(self) -> None:
        self.user1 = Subscriber('John')
        self.user2 = Subscriber('Smit')
        self.digital_magazine = DigitalMagazine()

    def test1_attach_subscribers(self):
        # Add 2 subscribers.
        self.assertEqual(self.digital_magazine.count_subscribers(), 0)
        self.digital_magazine.attach(self.user1)
        self.digital_magazine.attach(self.user2)
        self.assertEqual(self.digital_magazine.count_subscribers(), 2)

    def test2_detach_subscriber(self):
        # Add 2 subscribers then remove 1.
        self.assertEqual(self.digital_magazine.count_subscribers(), 0)
        self.digital_magazine.attach(self.user1)
        self.digital_magazine.attach(self.user2)
        self.assertEqual(self.digital_magazine.count_subscribers(), 2)
        self.digital_magazine.detach(self.user1)
        self.assertEqual(self.digital_magazine.count_subscribers(), 1)

    def test3_notify_to_subscribers(self):
        # Test that notifications reach subscribers.
        self.digital_magazine.attach(self.user1)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.digital_magazine.notify(title='Any Title', description='Any Description', url='http://localhost')
            print_output = fakeOutput.getvalue().strip()
            self.assertIn('John', print_output)
            self.assertIn('Any Title', print_output)
            self.assertIn('Any Description', print_output)
            self.assertIn('http://localhost', print_output)
