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

def test_vertical_movement_keeps_facing(self):
    boy = Boy()
    boy.press("left")
    boy.update(0.05)
    boy.release("left")
    boy.press("up")
    boy.update(0.05)
    self.assertEqual(boy.facing, "left")
    self.assertEqual(boy.clip()[1], 0)

def test_releasing_last_direction_returns_to_idle(self):
    boy = Boy()
    boy.press("right")
    boy.update(0.05)
    self.assertTrue(boy.moving)
    boy.release("right")
    boy.update(0.05)
    self.assertFalse(boy.moving)
    self.assertEqual(boy.clip()[1], 300)

def test_animation_advances_and_resets_on_state_change(self):
    boy = Boy()
    boy.update(0.05)
    boy.update(0.05)
    self.assertEqual(boy.frame, 1)
    boy.press("left")
    boy.update(0.05)
    self.assertEqual(boy.frame, 0)
    self.assertEqual(boy.clip()[1], 0)


if __name__ == "__main__":
    unittest.main()
