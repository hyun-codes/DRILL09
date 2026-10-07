"""화면 없이 소년 이동과 애니메이션을 검증한다."""

import math
import unittest

from boy_movement import Boy, CANVAS_HEIGHT, CANVAS_WIDTH, FRAME_SIZE


class BoyMovementTests(unittest.TestCase):
    def test_four_cardinal_directions(self):
        for direction, expected in {
            "left": (-1, 0), "right": (1, 0),
            "up": (0, 1), "down": (0, -1),
        }.items():
            with self.subTest(direction=direction):
                boy = Boy()
                boy.press(direction)
                boy.update(0.05)
                self.assertEqual((math.copysign(1, boy.x - CANVAS_WIDTH / 2) if boy.x != CANVAS_WIDTH / 2 else 0,
                                  math.copysign(1, boy.y - CANVAS_HEIGHT / 2) if boy.y != CANVAS_HEIGHT / 2 else 0), expected)

    def test_diagonal_directions_keep_constant_speed(self):
        for horizontal in ("left", "right"):
            for vertical in ("up", "down"):
                with self.subTest(horizontal=horizontal, vertical=vertical):
                    boy = Boy()
                    boy.press(horizontal)
                    boy.press(vertical)
                    boy.update(0.05)
                    self.assertEqual(boy.x > CANVAS_WIDTH / 2, horizontal == "right")
                    self.assertEqual(boy.y > CANVAS_HEIGHT / 2, vertical == "up")
                    self.assertAlmostEqual(math.hypot(boy.x - CANVAS_WIDTH / 2,
                                                      boy.y - CANVAS_HEIGHT / 2), 15.0)


if __name__ == "__main__":
    unittest.main()
