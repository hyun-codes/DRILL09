"""방향키로 소년을 8방향으로 움직이는 Pico2D 과제 실행 파일."""

from time import perf_counter

from pico2d import (
    SDL_QUIT,
    SDL_KEYDOWN,
    SDLK_LEFT,
    SDLK_RIGHT,
    clear_canvas,
    close_canvas,
    delay,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)

from boy_movement import Boy, CANVAS_HEIGHT, CANVAS_WIDTH

KEY_NAMES = {
    SDLK_LEFT: "left",
    SDLK_RIGHT: "right",
}


def run() -> None:
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        background = load_image("TUK_GROUND.png")
        sprite = load_image("animation_sheet.png")
        boy = Boy()
        running = True
        previous_time = perf_counter()

        while running:
            now = perf_counter()
            dt = now - previous_time
            previous_time = now

            for event in get_events():
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN:
                    direction = KEY_NAMES.get(event.key)
                    if direction:
                        boy.press(direction)

            boy.update(dt)

            clear_canvas()
            background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            source_x, source_y, width, height = boy.clip()
            sprite.clip_draw(source_x, source_y, width, height, boy.x, boy.y)
            update_canvas()
            delay(1 / 60)
    finally:
        close_canvas()


if __name__ == "__main__":
    run()
