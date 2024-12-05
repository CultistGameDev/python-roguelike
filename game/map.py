import random

import pygame

from game import BSP
from game.bsp import Node


class MapGen:
    def __init__(
        self,
        rows: int,
        cols: int,
        min_room: tuple[int, int],
        max_room: tuple[int, int],
        /,
        recurs: int = 3,
    ):
        self.bsp: BSP = BSP(recurs)
        self.rows: int = rows
        self.cols: int = cols
        self.min_room: tuple[int, int] = min_room
        self.max_room: tuple[int, int] = max_room
        self.rand = random.Random()

    def _gen_rooms(self, node: Node):
        if node.left and node.right:
            self._gen_rooms(node.left)
            self._gen_rooms(node.right)
        max_w, max_h = self.max_room
        min_w, min_h = self.min_room

        w = self.rand.randrange(min_w, max_w)
        h = self.rand.randrange(min_h, max_h)
