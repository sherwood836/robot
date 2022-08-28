import unittest
import mock
from robot import turn_right, turn_left, move_1, make_move, take_trip, \
                  program, error_check_start, error_check_max, \
                  error_check_coordinate

class RobotTest(unittest.TestCase):
    def test_turn_right(self):
        self.assertEqual((0, 0, 'S'), turn_right(0, 0, 'E'))
        self.assertEqual((0, 0, 'E'), turn_right(0, 0, 'N'))
        self.assertEqual((0, 0, 'N'), turn_right(0, 0, 'W'))
        self.assertEqual((0, 0, 'W'), turn_right(0, 0, 'S'))

    def test_turn_left(self):
        self.assertEqual((0, 0, 'S'), turn_left(0, 0, 'W'))
        self.assertEqual((0, 0, 'E'), turn_left(0, 0, 'S'))
        self.assertEqual((0, 0, 'N'), turn_left(0, 0, 'E'))
        self.assertEqual((0, 0, 'W'), turn_left(0, 0, 'N'))

    def test_move_1(self):
        self.assertEqual((1, 0, 'S'), move_1(1, 1, 'S', 5, 5))
        self.assertEqual((1, 0, 'E'), move_1(0, 0, 'E', 5, 5))
        self.assertEqual((0, 1, 'N'), move_1(0, 0, 'N', 5, 5))
        self.assertEqual((0, 1, 'W'), move_1(1, 1, 'W', 5, 5))

    def test_make_move(self):
        self.assertEqual((1, 3, 'W'), make_move(1, 3, 'N','L', 5, 5))
        self.assertEqual((1, 4, 'N'), make_move(1, 3, 'N','M', 5, 5))
        self.assertEqual((1, 3, 'E'), make_move(1, 3, 'N','R', 5, 5))

        with self.assertRaisesRegex(Exception, r'Invalid move:\[E\]'):
            make_move(1, 3, 'N','E', 5, 5)

    def test_take_trip(self):
        self.assertEqual((1, 3, 'N'), take_trip(1, 2, 'N', 'LMLMLMLMM', 5, 5))
        self.assertEqual((5, 1, 'E'), take_trip(3, 3, 'E', 'MMRMMRMRRM', 5, 5))

        self.assertEqual((1, 5, 'N'), take_trip(1, 2, 'N', 'LMLMLMLMMMMM', 5, 5))
        self.assertEqual((5, 1, 'E'), take_trip(3, 3, 'E', 'MMRMMRMRRMM', 5, 5))

    @mock.patch('builtins.input')
    def test_program(self, mock_read_line):
        mock_read_line.side_effect = ['5 5',
                                        '1 2 N',
                                        'LMLMLMLMM',
                                        '']

        self.assertEqual(['1 3 N'], program())

        mock_read_line.side_effect = ['5 5',
                                        '1 2 N',
                                        'LMLMLMLMM',
                                        '3 3 E',
                                        'MMRMMRMRRM',
                                        '']

        self.assertEqual(['1 3 N', '5 1 E'], program())

        with self.assertRaisesRegex(Exception, r'Invalid max coordinates given:\[5\]'):
            mock_read_line.side_effect = ['5',
                                            '1 2 N',
                                            'LMLMLMLMM',
                                            '3 3 E',
                                            'MMRMMRMRRM',
                                            '']

            program()

        mock_read_line.side_effect = ['5 5',
                                        '1 2 N',
                                        'LMLMLMLMMMMM',
                                        '3 3 E',
                                        'MMRMMRMRRMMMM',
                                        '']

        self.assertEqual(['1 5 N', '5 1 E'], program())

        mock_read_line.side_effect = ['5 5',
                                        '1 2 N',
                                        'LMMMLMLMLMMMMM',
                                        '3 3 E',
                                        'MMRMMMMRMRRMMMM',
                                        '']

        self.assertEqual(['1 5 N', '5 0 E'], program())

    def test_error_check_start(self):
        self.assertEqual((1, 3, 'N'), error_check_start("1 3 N", 5, 5))

        with self.assertRaisesRegex(Exception, r'Invalid start position:\[1\]'):
            error_check_start("1", 5, 5)

        with self.assertRaisesRegex(Exception, r'Invalid start position x coordinate:\[N\]'):
            error_check_start("N 2 N", 5, 5)

        with self.assertRaisesRegex(Exception, r'Invalid start position y coordinate:\[N\]'):
            error_check_start("1 N N", 5, 5)

        with self.assertRaisesRegex(Exception, r'Invalid start position x coordinate:\[-1\]'):
            error_check_start("-1 2 N", 5, 5)

        with self.assertRaisesRegex(Exception, r'Invalid start position y coordinate:\[-3\]'):
            error_check_start("1 -3 N", 5, 5)

        with self.assertRaisesRegex(Exception, r'Invalid start position direction:\[Tom\]'):
            error_check_start("1 2 Tom", 5, 5)

        with self.assertRaisesRegex(Exception, r'Invalid start position x coordinate:\[6\]'):
            error_check_start("6 2 N", 5, 5)

        with self.assertRaisesRegex(Exception, r'Invalid start position y coordinate:\[8\]'):
            error_check_start("1 8 N", 5, 5)

        self.assertEqual(None, error_check_start("", 5, 5))

    def test_error_check_max(self):
        self.assertEqual((5, 5), error_check_max("5 5"))

        with self.assertRaisesRegex(Exception, r'Invalid max coordinates given:\[1\]'):
            error_check_max("1")

        with self.assertRaisesRegex(Exception, r'Invalid max x coordinate:\[N\]'):
            error_check_max("N 2")

        with self.assertRaisesRegex(Exception, r'Invalid max y coordinate:\[N\]'):
            error_check_max("1 N")

        with self.assertRaisesRegex(Exception, r'Invalid max x coordinate:\[-1\]'):
            error_check_max("-1 2")

        with self.assertRaisesRegex(Exception, r'Invalid max coordinates given:\[\]'):
            error_check_max("")

    def test_error_check_coordinate(self): # A little excessive...but made the max check easy.
        self.assertEqual(1, error_check_coordinate("1", 5, "Error"))

        with self.assertRaisesRegex(Exception, r'Invalid max coordinates given:\[-1\]'):
            error_check_coordinate("-1", 5, "Invalid max coordinates given")

        with self.assertRaisesRegex(Exception, r'Invalid max coordinates given:\[Tom\]'):
            error_check_coordinate("Tom", 5, "Invalid max coordinates given")

        with self.assertRaisesRegex(Exception, r'Invalid max coordinates given:\[6\]'):
            error_check_coordinate("6", 5, "Invalid max coordinates given")

        self.assertEqual(100, error_check_coordinate("100", None, "Invalid max coordinates given"))


if __name__ == '__main__':
    unittest.main()
