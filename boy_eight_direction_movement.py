"""방향키로 소년을 8방향으로 움직이는 Pico2D 과제 실행 파일."""

from time import perf_counter

from pico2d import (
    SDL_QUIT,
    clear_canvas,
    close_canvas,
    delay,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024


def run() -> None:
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        background = load_image("TUK_GROUND.png")
        sprite = load_image("animation_sheet.png")
        running = True
        previous_time = perf_counter()

        while running:
            now = perf_counter()
            dt = now - previous_time
            previous_time = now

            for event in get_events():
                if event.type == SDL_QUIT:
                    running = False

            clear_canvas()
            background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            sprite.clip_draw(0, 300, 100, 100, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            update_canvas()
            delay(1 / 60)
    finally:
        close_canvas()


if __name__ == "__main__":
    run()
