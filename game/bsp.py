import random
import pygame


class Node:
    def __init__(self, *, root: bool = False):
        self.split: float = 0.0
        self.root: bool = root
        self.horziontal: bool = True
        self.left: Node | None = None
        self.right: Node | None = None


class BSP:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.root = Node(root=True)
        self.rand = random.Random()

    def draw(self, surf: pygame.Surface, width: int, height: int) -> None:
        self._draw(surf, width, height, (0, 0), self.root)

    def _draw(
        self,
        surf: pygame.Surface,
        width: int | float,
        height: int | float,
        corner: tuple[int | float, int | float],
        node: Node | None,
    ) -> None:
        if node:
            x, y = corner
            if node.horziontal:
                new_y = y + height * node.split
                pygame.draw.line(surf, (255, 255, 255), (x, new_y), (x + width, new_y))
                self._draw(surf, width, height * node.split, corner, node.left)
                self._draw(
                    surf,
                    width,
                    height * (1.0 - node.split),
                    (corner[0], corner[1] + height * node.split),
                    node.right,
                )
            else:
                new_x = x + width * node.split
                pygame.draw.line(surf, (255, 255, 255), (new_x, y), (new_x, y + height))
                self._draw(surf, width * node.split, height, corner, node.left)
                self._draw(
                    surf,
                    width * (1.0 - node.split),
                    height,
                    (corner[0] + width * node.split, corner[1]),
                    node.right,
                )

    def split(self, recur: int) -> None:
        self._split(self.root, recur)

    def _split(self, node: Node, recur: int, horizontal: bool = False) -> None:
        if recur >= 0:
            node.horziontal = horizontal
            node.split = self.rand.random() * (0.7 - 0.3) + 0.3
            node.left = Node()
            node.right = Node()
            self._split(node.left, recur - 1, not horizontal)
            self._split(node.right, recur - 1, not horizontal)
