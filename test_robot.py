import unittest
import mock
from robot import turn_right, turn_left, move_1, make_move, take_trip, program

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
        self.assertEqual((1, 0, 'S'), move_1(1, 1, 'S'))
        self.assertEqual((1, 0, 'E'), move_1(0, 0, 'E'))
        self.assertEqual((0, 1, 'N'), move_1(0, 0, 'N'))
        self.assertEqual((0, 1, 'W'), move_1(1, 1, 'W'))

        with self.assertRaisesRegex(Exception, r'Invalid direction:\[T\]'):
            move_1(1, 3, 'T')

    def test_make_move(self):
        self.assertEqual((1, 3, 'W'), make_move(1, 3, 'N','L'))
        self.assertEqual((1, 4, 'N'), make_move(1, 3, 'N','M'))
        self.assertEqual((1, 3, 'E'), make_move(1, 3, 'N','R'))

        with self.assertRaisesRegex(Exception, r'Invalid move:\[E\]'):
            make_move(1, 3, 'N','E')

    def test_take_trip(self):
        self.assertEqual((1, 3, 'N'), take_trip('1 2 N', 'LMLMLMLMM'))
        self.assertEqual((5, 1, 'E'), take_trip('3 3 E', 'MMRMMRMRRM'))

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

if __name__ == '__main__':
    unittest.main()
