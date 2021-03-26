from gamelib import Sprite
from dir_consts import *

class Dot(Sprite):
    def __init__(self, app, x, y):
        super().__init__(app, 'images/dot.png', x, y)

        self.is_eaten = False

    def get_eaten(self):
        self.is_eaten = True
        self.hide()


class Wall(Sprite):
    def __init__(self, app, x, y):
        super().__init__(app, 'images/wall.png', x, y)


class Maze:
    MAP = [
        "####################",
        "#..................#",
        "#.###.###..###.###.#",
        "#.#...#......#...#.#",
        "#.#.###.####.###.#.#",
        "#.#.#..........#.#.#",
        "#.....###..###.....#",
        "#.#.#..........#.#.#",
        "#.#.###.####.###.#.#",
        "#.#...#......#...#.#",
        "#.###.###..###.###.#",
        "#..................#",
        "####################",    
    ]

    WALL_CHAR = '#'
    DOT_CHAR = '.'

    def piece_center(self, r, c):
        return (c*40 + 20, 60 + (r * 40))

    def is_at_center(self, x, y):
        return ((x - 20) % 40 == 0) and ((y - 60) % 40 == 0)

    def xy_to_rc(self, x, y):
        return ((y - 60) // 40, (x - 20) // 40)

    def init_active_dots(self):
        self.has_active_dots = {}
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                self.has_active_dots[(i,j)] = Maze.MAP[i][j] == Maze.DOT_CHAR

    def init_maze_sprites(self):
        self.walls = []
        self.dots = {}

        self.init_active_dots()

        for i in range(self.get_height()):
            for j in range(self.get_width()):
                x, y = self.piece_center(i, j)

                if self.has_wall_at(i, j):
                    wall = Wall(self.app, x, y)
                    self.walls.append(wall)

                if self.has_dot_at(i, j):
                    dot = Dot(self.app, x, y)
                    self.dots[(i,j)] = dot

    def __init__(self, app, canvas_width, canvas_height):
        self.app = app
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.init_maze_sprites()

    def init_element(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def has_wall_at(self, r, c):
        return Maze.MAP[r][c] == Maze.WALL_CHAR

    def has_dot_at(self, r, c):
        if (r,c) in self.has_active_dots:
            return self.has_active_dots[(r,c)]
        else:
            return False

    def eat_dot_at(self, r, c):
        dot = self.dots[(r,c)]
        dot.get_eaten()

        self.has_active_dots[(r,c)] = False

    def is_movable_direction(self, r, c, direction):
        nr = r + DIR_RC_OFFSET[direction][0]
        nc = c + DIR_RC_OFFSET[direction][1]

        if (nc < 0) or (nr < 0) or (nc >= self.get_width()) or (nr >= self.get_height()):
            return False

        return not self.has_wall_at(nr, nc)

    def get_height(self):
        return len(Maze.MAP)

    def get_width(self):
        return len(Maze.MAP[0])

