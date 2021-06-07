import unittest

from d_graph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):
    def test_add_vertex_example_1(self) -> None:
        # Arrange
        exp: list = [[0] * 5] * 5
        g: DirectedGraph = DirectedGraph()

        # Act
        for _ in range(5):
            g.add_vertex()

        # Assert
        self.assertListEqual(exp, g.adj_matrix)

    def test_add_edge_example_1(self) -> None:
        # Arrange
        exp: list = [
            [0, 10, 0, 0, 0],
            [0, 0, 0, 0, 15],
            [0, 23, 0, 0, 0],
            [0, 5, 7, 0, 0],
            [12, 0, 0, 3, 0]
        ]
        g: DirectedGraph = DirectedGraph()
        for _ in range(5):
            g.add_vertex()

        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]

        # Act
        for src, dst, weight in edges:
            g.add_edge(src, dst, weight)

        # Assert
        self.assertListEqual(exp, g.adj_matrix)

    def test_remove_edge_does_nothing_if_edge_invalid(self) -> None:
        # Arrange
        exp: list = [[0] * 5] * 5
        g: DirectedGraph = DirectedGraph()
        for _ in range(5):
            g.add_vertex()

        # Act
        g.remove_edge(0, 5)

        # Assert
        self.assertListEqual(exp, g.adj_matrix)

    def test_remove_edge_updates_edge_if_valid(self) -> None:
        # Arrange
        exp: list = [
            [0, 10, 0, 0, 0],
            [0, 0, 0, 0, 15],
            [0, 0, 0, 0, 0],
            [0, 5, 7, 0, 0],
            [12, 0, 0, 3, 0]
        ]
        g: DirectedGraph = DirectedGraph()
        for _ in range(5):
            g.add_vertex()

        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        for src, dst, weight in edges:
            g.add_edge(src, dst, weight)

        # Act
        g.remove_edge(2, 1)

        # Assert
        self.assertListEqual(exp, g.adj_matrix)

    def test_is_valid_edge_returns_true_if_valid(self) -> None:
        # Arrange
        g: DirectedGraph = DirectedGraph()
        for _ in range(2):
            g.add_vertex()

        # Act/Assert
        self.assertTrue(g._is_valid_edge(0, 1))
        self.assertTrue(g._is_valid_edge(1, 0))

    def test_is_valid_edge_returns_false_if_valid(self) -> None:
        # Arrange
        g: DirectedGraph = DirectedGraph()
        for _ in range(2):
            g.add_vertex()

        # Act/Assert
        self.assertFalse(g._is_valid_edge(0, 0))
        self.assertFalse(g._is_valid_edge(1, 1))
        self.assertFalse(g._is_valid_edge(0, 2))
        self.assertFalse(g._is_valid_edge(2, 0))
        self.assertFalse(g._is_valid_edge(2, 2))

    def test_get_vertices_example_1(self) -> None:
        # Arrange
        exp: list = [0, 1, 2, 3, 4]
        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g: DirectedGraph = DirectedGraph(edges)

        # Act
        vertices: list = g.get_vertices()

        # Assert
        self.assertListEqual(exp, vertices)


if __name__ == "__main__":
    unittest.main()
