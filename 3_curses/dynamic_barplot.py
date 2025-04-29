import curses
import time

LABELS = ['node 1', 'node 2', 'node 3']
VALUES_ALL = [[10, 20, 15], [12, 18, 17], [8, 17, 4]]

BOX_OFFSET_X = 6
BOX_OFFSET_Y = 3
BOX_HEIGHT = 21
BOX_WIDTH = 35
BAR_SPACING = 11
BAR_WIDTH = 4


def draw_box(stdscr, x1, x2, y1, y2, color):
    stdscr.addch(y1, x1, curses.ACS_ULCORNER | color)
    stdscr.addch(y1, x2, curses.ACS_URCORNER | color)
    stdscr.addch(y2, x2, curses.ACS_LRCORNER | color)
    stdscr.addch(y2, x1, curses.ACS_LLCORNER | color)
    for x in range(x1 + 1, x2):
        stdscr.addch(y1, x, curses.ACS_HLINE | color)
        stdscr.addch(y2, x, curses.ACS_HLINE | color)
    for y in range(y1 + 1, y2):
        stdscr.addch(y, x1, curses.ACS_VLINE | color)
        stdscr.addch(y, x2, curses.ACS_VLINE | color)


def draw_bar(stdscr, base_y, col, height, color):
    for h in range(height):
        for w in range(BAR_WIDTH):
            stdscr.addstr(base_y - h, col + w, " ", color)


def draw_vertical_bars(stdscr):
    curses.curs_set(0)

    # Color setup
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, 197)
    curses.init_pair(3, curses.COLOR_BLACK, 40)
    curses.init_pair(4, curses.COLOR_BLACK, 32)

    box_color = curses.color_pair(1)
    bar_colors = [curses.color_pair(i + 2) for i in range(len(LABELS))]

    max_value = max(max(values) for values in VALUES_ALL)
    max_bar_height = BOX_HEIGHT - 1
    base_y = BOX_OFFSET_Y + BOX_HEIGHT - 1

    cycle_index = 0

    while True:
        stdscr.clear()
        values = VALUES_ALL[cycle_index % len(VALUES_ALL)]
        cycle_index += 1

        # title
        stdscr.addstr(1, 18, "SYSTEM LOAD", curses.A_BOLD)

        # draw box and Y-axis labels
        draw_box(stdscr, BOX_OFFSET_X, BOX_OFFSET_X + BOX_WIDTH, BOX_OFFSET_Y, BOX_OFFSET_Y + BOX_HEIGHT, box_color)
        stdscr.addstr(BOX_OFFSET_Y + 1, BOX_OFFSET_X - 5, "100%")
        stdscr.addstr(BOX_OFFSET_Y + BOX_HEIGHT - 1, BOX_OFFSET_X - 3, "0%")

        # draw bars
        for i, (label, value) in enumerate(zip(LABELS, values)):
            bar_height = int((value / max_value) * max_bar_height)
            col = BOX_OFFSET_X + 5 + i * BAR_SPACING
            draw_bar(stdscr, base_y, col, bar_height, bar_colors[i])
            stdscr.addstr(base_y + 2, col - 1, label)

        stdscr.refresh()
        time.sleep(0.5)


if __name__ == "__main__":
    curses.wrapper(draw_vertical_bars)
