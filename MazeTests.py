import unittest
import turtle
from Maze import Maze

SIZE = 400

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class MazeTests(unittest.TestCase):
    def setUp(self):
        self.m = Maze()

    def testScreen(self):
        self.assertTrue(type(self.m.s) == turtle._Screen, "No Screen!")

    def testTurtle(self):
        self.assertTrue(type(self.m.turtle) == turtle.Turtle)

    def testBackground(self):
        self.assertTrue(self.m.s.bgcolor() == 'blue')

    def testSize(self):
        self.assertTrue(self.m.s.window_height() == SIZE * 1.3, f"window height is {self.m.s.window_height()}")
        self.assertTrue(self.m.s.window_width() == SIZE * 1.3)

    def testMatrixSize(self):
        self.assertTrue(len(self.m.matrix) == SIZE / 20)

    def testReset(self):
        self.m.reset()
        self.assertTrue(self.m.turtle.pos() == (-(SIZE / 2 - 20), SIZE / 2 - 20))

    def testCoordinates(self):
        self.m.turtle.goto(-180, 180)
        self.m.turtle.stamp()
        self.m.turtle.goto(-180, -200)
        self.m.turtle.stamp()
        self.m.turtle.goto(200, -200)
        self.m.turtle.stamp()
        self.m.turtle.goto(200, 180)
        self.m.turtle.stamp()
        self.assertTrue((0, 0) == self.m.pos2index((-180, 180)), f"{self.m.pos2index((-180, 180))}")
        self.assertTrue((19, 19) == self.m.pos2index((200, -200)), f"{self.m.pos2index((200, -200))}")

    def testSettingMatrixValues(self):
        self.m.reset()
        value = self.m.getMatrixValueAt(self.m.turtle.position())
        self.assertTrue(0 == value)
        value = 1
        self.m.setMatrixValueAt(self.m.turtle.position(), value)
        self.assertEqual(self.m.matrix[0][0], 1)
        self.m.turtle.goto(-160, 180)
        value = self.m.getMatrixValueAt(self.m.turtle.position())
        self.assertTrue(1 == value)
        value = 0
        self.m.setMatrixValueAt(self.m.turtle.position(), value)
        self.assertEqual(self.m.matrix[0][1], 0)
        self.m.turtle.goto(200, -200)
        value = self.m.getMatrixValueAt(self.m.turtle.position())
        self.assertTrue(1 == value)
        value = 0
        self.m.setMatrixValueAt(self.m.turtle.position(), value)
        self.assertTrue(0 == value)

    def testSetMatrixValueAt(self):
        self.m.setMatrixValueAt(self.m.turtle.pos(), 1)
        self.assertTrue(self.m.matrix[0][0] == 1)
        self.m.setMatrixValueAt(self.m.turtle.pos(), 0)
        self.assertTrue(self.m.matrix[0][0] == 0)

    def testDig(self):
        self.m.dig(EAST)
        self.assertEqual(self.m.turtle.pos(), (-160, 180))
        self.assertTrue(self.m.matrix[1][0] == 0)
        self.m.dig(WEST)
        self.assertEqual(self.m.turtle.pos(), (-180, 180))
        self.m.dig(NORTH)
        self.assertEqual(self.m.turtle.pos(), (-180, 180))
        self.m.dig(SOUTH)
        self.assertEqual(self.m.turtle.pos(), (-180, 160))

    def testBreakThrough(self):
        self.m.dig(EAST)
        self.m.dig(EAST)
        self.m.dig(EAST)
        self.m.dig(EAST)
        self.m.dig(SOUTH)
        self.m.dig(SOUTH)
        self.m.dig(WEST)
        self.m.dig(WEST)
        self.m.dig(NORTH)
        self.assertTrue(self.m.turtle.pos() == (-140, 140),f"{self.m.turtle.pos()}")

    def testBreakThrough2(self):
        self.m.dig(SOUTH)
        self.m.dig(SOUTH)
        self.m.dig(SOUTH)
        self.m.dig(SOUTH)
        self.m.dig(EAST)
        self.m.dig(EAST)
        self.m.dig(NORTH)
        self.m.dig(NORTH)
        self.m.dig(WEST)
        self.assertTrue(self.m.turtle.pos() == (-140, 140), f"{self.m.turtle.pos()}")


    # def testNeighbors(self):
    #     self.assertTrue(self.m.neighbors() == [(1, 0), (-1, 1), (-1, 2), (1, 3)], f"{self.m.neighbors()}")
    #     r = self.m.neighbors()
    #     self.assertTrue((r[0] == (1, 0) and r[1] == (-1, 1) and
    #                      r[2] == (-1, 2) and r[3] == (1, 3)), "got " + str(r))
    #     self.m.reset()
    #     self.m.turtle.goto(-160, 160)
    #     r = self.m.neighbors()
    #     self.assertTrue((r[0] == (1, 0) and r[1] == (-1, 1) and
    #                      r[2] == (-1, 2) and r[3] == (1, 3)), "got " + str(r))
    #     self.m.reset()
    #     self.m.turtle.goto(-140, 140)
    #     r = self.m.neighbors()
    #     self.assertTrue((r[0] == (1, 0) and r[1] == (1, 1) and
    #                      r[2] == (1, 2) and r[3] == (1, 3)), "got " + str(r))

if __name__ == "__main__":
    unittest.main()
