"""실제 창을 열지 않고 게임 루프의 입력과 그리기 연결을 검증한다."""

import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import Drill09_movement as game


class GameLoopTests(unittest.TestCase):
    def test_diagonal_input_reaches_sprite_and_resources_are_loaded(self):
        background = Mock()
        sprite = Mock()
        events = [
            [SimpleNamespace(type=game.SDL_KEYDOWN, key=game.SDLK_LEFT),
             SimpleNamespace(type=game.SDL_KEYDOWN, key=game.SDLK_UP)],
            [SimpleNamespace(type=game.SDL_KEYUP, key=game.SDLK_LEFT),
             SimpleNamespace(type=game.SDL_KEYUP, key=game.SDLK_UP)],
            [SimpleNamespace(type=game.SDL_QUIT)],
        ]
        with patch.object(game, "open_canvas") as open_canvas, \
             patch.object(game, "close_canvas") as close_canvas, \
             patch.object(game, "load_image", side_effect=[background, sprite]) as load_image, \
             patch.object(game, "get_events", side_effect=events), \
             patch.object(game, "perf_counter", side_effect=[0.0, 0.05, 0.10, 0.15]), \
             patch.object(game, "clear_canvas"), \
             patch.object(game, "update_canvas"), \
             patch.object(game, "delay"):
            game.run()

        open_canvas.assert_called_once_with(1280, 1024)
        self.assertEqual(load_image.call_args_list[0].args, ("TUK_GROUND.png",))
        self.assertEqual(load_image.call_args_list[1].args, ("animation_sheet.png",))
        background.draw.assert_called_with(640, 512)
        first_draw = sprite.clip_draw.call_args_list[0].args
        self.assertEqual(first_draw[:4], (0, 0, 100, 100))
        self.assertLess(first_draw[4], 640)
        self.assertGreater(first_draw[5], 512)
        close_canvas.assert_called_once()

    def test_escape_closes_canvas(self):
        with patch.object(game, "open_canvas"), \
             patch.object(game, "close_canvas") as close_canvas, \
             patch.object(game, "load_image", side_effect=[Mock(), Mock()]), \
             patch.object(game, "get_events", return_value=[SimpleNamespace(
                 type=game.SDL_KEYDOWN, key=game.SDLK_ESCAPE)]), \
             patch.object(game, "perf_counter", side_effect=[0.0, 0.05]), \
             patch.object(game, "clear_canvas"), \
             patch.object(game, "update_canvas"), \
             patch.object(game, "delay"):
            game.run()

        close_canvas.assert_called_once()


if __name__ == "__main__":
    unittest.main()
