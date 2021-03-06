# -*-coding:utf-8 -*


class Mac:
    """
    Class's docstring
    """

    def __init__(self, maze):
        self.mac_x = int()
        self.mac_y = int()
        self.maze = maze
        self.front_g = False

    def mac_down(self):

        if self.mac_y < 14 and self.maze[self.mac_y + 1][self.mac_x] == "G":
            self.front_g = True
        elif self.mac_y < 14 and self.maze[self.mac_y + 1][self.mac_x] == "@":
            self.mac_y += 1
            return self.mac_x, self.mac_y
        else:
            return self.mac_x, self.mac_y

    def mac_up(self):

        if self.mac_y > 0 and self.maze[self.mac_y - 1][self.mac_x] == "G":
            self.front_g = True
        elif self.mac_y > 0 and self.maze[self.mac_y - 1][self.mac_x] == "@" \
                or self.maze[self.mac_y - 1][self.mac_x] == "M":
            self.mac_y -= 1
            return self.mac_x, self.mac_y
        else:
            return self.mac_x, self.mac_y

    def mac_right(self):
        if self.mac_x < 14 and self.maze[self.mac_y][self.mac_x + 1] == "G":
            self.front_g = True
        elif self.mac_x < 14 and self.maze[self.mac_y][self.mac_x + 1] == "@":
            self.mac_x += 1
            return self.mac_x, self.mac_y
        else:
            return self.mac_x, self.mac_y

    def mac_left(self):
        if self.mac_x > 0 and self.maze[self.mac_y][self.mac_x - 1] == "G":
            self.front_g = True
        elif self.mac_x > 0 and self.maze[self.mac_y][self.mac_x - 1] == "@" \
                or self.maze[self.mac_y - 1][self.mac_x - 1] == "M":
            self.mac_x -= 1
            return self.mac_x, self.mac_y
        else:
            return self.mac_x, self.mac_y
