import random
import pygame


class Node:
    """
    A Binary Tree Node for the BSP class.
    """

    def __init__(self, *, root: bool = False):
        """
        Create a node which is denoted as the root node if `root` is True

        Args:
            root (bool, optional): Whether the node being created is the root. Defaults to False.
        """
        self.split: float = 0.0
        self.root: bool = root
        self.horziontal: bool = True
        self.left: Node | None = None
        self.right: Node | None = None


class BSP:
    """
    Class that allows for the creation of a map using a Binary Space Partition Tree.
    """

    def __init__(
        self, recur: int, /, max_split: float = 0.7, min_split: float = 0.3
    ) -> None:
        """
        Creates the BSP class.
        """
        self.root = Node(root=True)
        self.rand = random.Random()
        self.max_split = max_split
        self.min_split = min_split
        self._split(self.root, recur, bool(self.rand.getrandbits(1)))

    def draw(self, surf: pygame.Surface, width: int, height: int) -> None:
        """
        Draws the current BSP onto the pygame surface `surf`.

        Args:
            surf (pygame.Surface): The surface to draw to.
            width (int): Width of `surf`
            height (int): Height of `surf`
        """
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

    def _split(self, node: Node, recur: int, horizontal: bool) -> None:
        if recur >= 0:
            node.horziontal = horizontal
            node.split = (
                self.rand.random() * (self.max_split - self.min_split) + self.min_split
            )
            node.left = Node()
            node.right = Node()
            self._split(node.left, recur - 1, not horizontal)
            self._split(node.right, recur - 1, not horizontal)
