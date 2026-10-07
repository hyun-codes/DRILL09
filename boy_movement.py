"""소년의 입력, 이동, 애니메이션을 화면 처리와 분리한 상태 모델."""

from dataclasses import dataclass, field
from math import hypot

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
FRAME_SIZE = 100
FRAME_COUNT = 8
FRAME_DURATION = 0.1
MOVE_PER_FRAME = 5.0
DIRECTIONS = frozenset({"left", "right", "up", "down"})


@dataclass
class Boy:
    x: float = CANVAS_WIDTH / 2
    y: float = CANVAS_HEIGHT / 2
    held: set[str] = field(default_factory=set)
    facing: str = "right"
    moving: bool = False
    frame: int = 0
    frame_time: float = 0.0

    def press(self, direction: str) -> None:
        if direction not in DIRECTIONS:
            return
        self.held.add(direction)
        if direction in ("left", "right"):
            self.facing = direction

    def update(self, dt: float) -> None:
        dx = int("right" in self.held) - int("left" in self.held)
        dy = int("up" in self.held) - int("down" in self.held)
        distance = MOVE_PER_FRAME
        length = hypot(dx, dy)
        if length:
            self.x += dx / length * distance
            self.y += dy / length * distance

    def clip(self) -> tuple[int, int, int, int]:
        return 0, 3 * FRAME_SIZE, FRAME_SIZE, FRAME_SIZE
