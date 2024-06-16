from tlib.game.engine import TanuGameEngine
from tlib.graphics.graphics import BGRA

def main():
    tanu = TanuGameEngine(
        base_background_fill_color=BGRA(0, 0, 0),
        start_after_right_after_init=True
    )


if __name__ == "__main__":
    main()