import unittest

from ud_graph import UndirectedGraph


class TestUDGraph(unittest.TestCase):
    def test_add_vertex_example_1(self) -> None:
        # Arrange
        exp: dict = {'A': ["new"], 'B': [], 'C': [], 'D': [], 'E': []}
        g: UndirectedGraph = UndirectedGraph()

        # Act
        for v in "ABCDE":
            g.add_vertex(v)

        # Ensure existing vertex is not overwritten.
        g.adj_list['A'].append("new")
        g.add_vertex('A')

        # Assert
        self.assertDictEqual(exp, g.adj_list)

    def test_add_edge_example_1(self) -> None:
        # Arrange
        exp: dict = {'A': ['B', 'C'],
                     'B': ['A', 'C', 'D'],
                     'C': ['A', 'B', 'D', 'E'],
                     'D': ['B', 'C', 'E'],
                     'E': ['C', 'D']}

        g: UndirectedGraph = UndirectedGraph()

        for v in 'ABCDE':
            g.add_vertex(v)

        # Act
        for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
            g.add_edge(u, v)

        # Assert
        self.assertDictEqual(exp, g.adj_list)

    def test_add_edge_does_nothing_if_vertices_are_the_same(self) -> None:
        # Arrange
        exp: dict = {'A': []}
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')

        # Act
        g.add_edge('A', 'A')

        # Assert
        self.assertDictEqual(exp, g.adj_list)

    def test_degree_returns_degree_of_vertex_if_it_exists(self) -> None:
        # Arrange
        exp: int = 2
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        g.add_edge('A', 'B')
        g.add_edge('A', 'C')

        # Act
        deg: int = g.degree('A')

        # Assert
        self.assertEqual(exp, deg)

    def test_degree_returns_neg_one_if_vertex_does_not_exist(self) -> None:
        # Arrange
        exp: int = -1
        g: UndirectedGraph = UndirectedGraph()

        # Act
        deg: int = g.degree('A')

        # Assert
        self.assertEqual(exp, deg)

    def test_are_adjacent_returns_true_if_vertices_adjacent(self) -> None:
        # Arrange
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')

        g.add_edge('A', 'B')

        # Act
        adj: bool = g.are_adjacent('A', 'B')

        # Assert
        self.assertTrue(adj)

    def test_are_adjacent_returns_false_if_vertices_not_adjacent(self) -> None:
        # Arrange
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        g.add_edge('A', 'B')

        # Act
        adj: bool = g.are_adjacent('A', 'C')

        # Assert
        self.assertFalse(adj)

    def test_are_adjacent_returns_false_if_one_or_more_vertices_dont_exist(self) -> None:
        # Arrange
        g: UndirectedGraph = UndirectedGraph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        # Act
        adj_1: bool = g.are_adjacent('A', 'D')
        adj_2: bool = g.are_adjacent('D', 'E')

        # Assert
        self.assertFalse(adj_1)
        self.assertFalse(adj_2)

    def test_remove_vertex_example_1(self) -> None:
        # Arrange
        exp: dict = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'E'], 'E': ['C']}
        g: UndirectedGraph = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])

        # Act
        g.remove_vertex('DOES NOT EXIST')
        g.remove_vertex('D')

        # Assert
        self.assertDictEqual(exp, g.adj_list)

    def test_remove_edge_example_1(self) -> None:
        # Arrange
        exp: dict = {'A': ['C'], 'B': ['C', 'D'], 'C': ['A', 'B', 'D', 'E'], 'D': ['B', 'C', 'E'], 'E': ['C', 'D']}
        g: UndirectedGraph = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])

        # Act
        g.remove_edge('A', 'B')
        g.remove_edge('X', 'B')

        # Assert
        self.assertDictEqual(exp, g.adj_list)

    def test_get_vertices_example_1(self) -> None:
        # Arrange
        exp_1: list = []
        g_1: UndirectedGraph = UndirectedGraph()

        exp_2: list = ['A', 'B', 'C', 'D', 'E']
        g_2: UndirectedGraph = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])

        # Act
        vert_1: list = g_1.get_vertices()
        vert_2: list = g_2.get_vertices()

        # Assert
        self.assertListEqual(exp_1, vert_1)
        self.assertListEqual(exp_2, vert_2)

    def test_get_edges_example_1(self) -> None:
        # Arrange
        exp: list = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E')]
        g: UndirectedGraph = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])

        # Act
        edges: list = g.get_edges()

        # Assert
        self.assertCountEqual(exp, edges)

    def test_is_valid_path_example_1(self) -> None:
        # Arrange
        g: UndirectedGraph = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
        test_cases: list = [('ABC', True), ('ADE', False), ('ECABDCBE', False), ('ACDECB', True), ('', True),
                            ('D', True), ('Z', False)]

        # Act/Assert
        for path, exp in test_cases:
            valid: bool = g.is_valid_path(path)
            self.assertEqual(exp, valid)

    def test_dfs_example_1(self) -> None:
        # Arrange
        edges: list = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
        g: UndirectedGraph = UndirectedGraph(edges)
        test_cases: list = [
            ('A', None, ['A', 'C', 'B', 'D', 'E', 'H']),
            ('B', None, ['B', 'C', 'A', 'E', 'D', 'H']),
            ('C', None, ['C', 'A', 'E', 'B', 'D', 'H']),
            ('D', None, ['D', 'B', 'C', 'A', 'E', 'H']),
            ('E', None, ['E', 'A', 'C', 'B', 'D', 'H']),
            ('G', None, ['G', 'F', 'Q']),
            ('H', None, ['H', 'B', 'C', 'A', 'E', 'D']),
            ('B', 'G', ['B', 'C', 'A', 'E', 'D', 'H']),
            ('C', 'E', ['C', 'A', 'E']),
            ('D', 'D', ['D']),
            ('E', 'C', ['E', 'A', 'C']),
            ('G', 'B', ['G', 'F', 'Q']),
            ('H', 'A', ['H', 'B', 'C', 'A'])
        ]

        # Act/Assert
        for v_start, v_end, exp in test_cases:
            dfs: list = g.dfs(v_start, v_end)
            self.assertListEqual(exp, dfs)

    def test_bfs_example_1(self) -> None:
        # Arrange
        edges: list = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
        g: UndirectedGraph = UndirectedGraph(edges)
        test_cases: list = [
            ('A', None, ['A', 'C', 'E', 'B', 'D', 'H']),
            ('B', None, ['B', 'C', 'D', 'E', 'H', 'A']),
            ('C', None, ['C', 'A', 'B', 'D', 'E', 'H']),
            ('D', None, ['D', 'B', 'C', 'E', 'H', 'A']),
            ('E', None, ['E', 'A', 'B', 'C', 'D', 'H']),
            ('G', None, ['G', 'F', 'Q']),
            ('H', None, ['H', 'B', 'C', 'D', 'E', 'A']),
            ('B', 'G', ['B', 'C', 'D', 'E', 'H', 'A']),
            ('C', 'E', ['C', 'A', 'B', 'D', 'E']),
            ('D', 'D', ['D']),
            ('E', 'C', ['E', 'A', 'B', 'C']),
            ('G', 'B', ['G', 'F', 'Q']),
            ('H', 'A', ['H', 'B', 'C', 'D', 'E', 'A'])
        ]

        # Act/Assert
        for v_start, v_end, exp in test_cases:
            bfs: list = g.bfs(v_start, v_end)
            self.assertListEqual(exp, bfs)

    def test_connected_components_empty_graph_returns_empty_list(self) -> None:
        # Arrange
        exp: list = list()
        g: UndirectedGraph = UndirectedGraph()

        # Act
        comp: list = g.connected_components()

        # Assert
        self.assertEqual(exp, comp)

    def test_connected_components_graph_with_disconnected_vertices_returns_each_vertex_as_component(self) -> None:
        # Arrange
        exp: list = [['A'], ['B'], ['C']]
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        # Act
        comp: list = g.connected_components()

        # Assert
        self.assertCountEqual(exp, comp)

    def test_connected_components_connected_graph_returns_single_component(self) -> None:
        # Arrange
        exp: list = [['A', 'B', 'C']]
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('A', 'C')

        # Act
        comp: list = g.connected_components()

        # Assert
        self.assertEqual(len(exp), len(comp))
        self.assertCountEqual(exp[0], comp[0])

    def test_connected_components_disconnected_graph_returns_all_components(self) -> None:
        # Arrange
        exp: list = [['A', 'B', 'C'], ['D'], ['E', 'F']]
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_vertex('D')
        g.add_vertex('E')
        g.add_vertex('F')
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('A', 'C')
        g.add_edge('E', 'F')

        # Act
        comp: list = g.connected_components()

        # Assert
        self.assertEqual(len(exp), len(comp))
        i: int = 0
        while i < len(exp):
            self.assertCountEqual(sorted(exp)[i], sorted(comp)[i])
            i += 1

    def test_count_connected_components_example_1(self) -> None:
        # Arrange
        edges: list = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
        g: UndirectedGraph = UndirectedGraph(edges)
        test_cases: tuple = (
            ('add QH', 1),
            ('remove FG', 2),
            ('remove GQ', 3),
            ('remove HQ', 4),
            ('remove AE', 4),
            ('remove CA', 5),
            ('remove EB', 5),
            ('remove CE', 5),
            ('remove DE', 6),
            ('remove BC', 6),
            ('add EA', 5),
            ('add EF', 4),
            ('add GQ', 3),
            ('add AC', 2),
            ('add DQ', 1),
            ('add EG', 1),
            ('add QH', 1),
            ('remove CD', 1),
            ('remove BD', 1),
            ('remove QG', 2)
        )

        for case, exp in test_cases:
            command, edge = case.split()
            u, v = edge
            g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
            self.assertEqual(exp, g.count_connected_components())

    def test_has_cycle_example_1(self) -> None:
        # Arrange
        edges: list = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
        g: UndirectedGraph = UndirectedGraph(edges)
        test_cases: tuple = (
            ('add QH', True),
            ('remove FG', True),
            ('remove GQ', True),
            ('remove HQ', True),
            ('remove AE', True),
            ('remove CA', True),
            ('remove EB', True),
            ('remove CE', True),
            ('remove DE', True),
            ('remove BC', False),
            ('add EA', False),
            ('add EF', False),
            ('add GQ', False),
            ('add AC', False),
            ('add DQ', False),
            ('add EG', True),
            ('add QH', True),
            ('remove CD', True),
            ('remove BD', False),
            ('remove QG', False),
            ('add FG', True),
            ('remove GE', False)
        )

        for case, exp in test_cases:
            command, edge = case.split()
            u, v = edge
            g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
            self.assertEqual(exp, g.has_cycle())


if __name__ == "__main__":
    unittest.main()
