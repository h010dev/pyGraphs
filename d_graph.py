# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

from collections import deque


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    def add_vertex(self) -> int:
        """
        Adds new vertex to the graph.

        Returns new number of vertices in graph.
        """

        # Extend matrix by one column.
        for row in self.adj_matrix:
            row.append(0)

        # Extend matrix by one row.
        self.adj_matrix.append([0] * (self.v_count + 1))

        # Update vertex count.
        self.v_count += 1

        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds a new edge to the graph, connecting src vertex to dst vertex.

        If src and dst point to the same vertex, or if weight is not positive, does nothing and returns.
        If edge already exists, updates weight of edge.
        """

        # Only update weight if src and dst exist and don't point to same vertex and weight is positive.
        if self._is_valid_edge(src, dst) and weight >= 1:
            self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between src and dst vertices.

        If either vertex does not exist in the graph, or if there is no edge between them, does nothing and returns.
        """

        # Only remove edge if vertices exist.
        if self._is_valid_edge(src, dst):
            self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """Returns a list of vertices of the graph."""

        return [_ for _ in range(self.v_count)]

    def get_edges(self) -> []:
        """
        Returns a list of 3-tuples containing the source vertex, destination vertex, and edge weight for all edges
        in graph.
        """

        edges: list = list()

        for i in range(self.v_count):
            for j in range(self.v_count):
                # Edge exists between vertex i and j.
                if self.adj_matrix[i][j] > 0:
                    edges.append((i, j, self.adj_matrix[i][j]))

        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        Return True if the provided path is valid.

        An empty path or a path with a single vertex is considered valid.
        """

        # Check if path is empty or contains only a single vertex.
        if len(path) == 0:
            return True
        elif len(path) == 1:
            if 0 <= path[0] < self.v_count:
                return True
            else:
                return False

        # Iterate through vertices in path, checking if they are adjacent to each other so that they form a path.
        step: int = 0
        while step < len(path) - 1:
            src, dst = path[step], path[step + 1]
            if not self.are_adjacent(src, dst):
                return False

            step += 1

        return True

    def dfs(self, v_start: int, v_end: int = None) -> []:
        """
        Return list of vertices visited during DFS search from v_start vertex up to optional v_end vertex.

        If v_start is not in the graph, returns empty list.
        If v_end is not in the graph, will treat it as having no v_end parameter.

        Vertices are picked in ascending order.
        """

        visited: list = list()

        # Check if v_start is in graph.
        if not 0 <= v_start < self.v_count:
            return visited

        # Check if v_end is in graph.
        if isinstance(v_end, int) and not 0 <= v_end < self.v_count:
            v_end = None

        # Traverse graph until we either reach v_end or traverse every vertex.
        vertices: deque = deque()
        vertices.appendleft(v_start)
        while len(vertices) > 0:
            v: int = vertices.popleft()
            if v not in visited:
                # Add vertex to visited vertices.
                visited.append(v)

                # Stop if vertex is equal to v_end.
                if v == v_end:
                    break

                # Add all neighbors of vertex in descending order so that they are popped in ascending order.
                for neighbor in reversed(self.neighbors(v)):
                    vertices.appendleft(neighbor)

        return visited

    def bfs(self, v_start: int, v_end: int = None) -> []:
        """
        Return list of vertices visited during BFS search from v_start vertex up to optional v_end vertex.

        If v_start is not in the graph, returns empty list.
        If v_end is not in the graph, will treat it as having no v_end parameter.

        Vertices are picked in ascending order.
        """

        visited: list = list()

        # Check if v_start is in graph.
        if not 0 <= v_start < self.v_count:
            return visited

        # Check if v_end is in graph.
        if isinstance(v_end, int) and not 0 <= v_end < self.v_count:
            v_end = None

        # Traverse graph until we either reach v_end or traverse every vertex.
        vertices: deque = deque()
        vertices.appendleft(v_start)
        while len(vertices) > 0:
            v: int = vertices.pop()
            if v not in visited:
                # Add vertex to visited vertices.
                visited.append(v)

                # Stop if vertex is equal to v_end.
                if v == v_end:
                    break

                # Add all neighbors of vertex in descending order so that they are popped in ascending order.
                for neighbor in self.neighbors(v):
                    vertices.appendleft(neighbor)

        return visited

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        pass

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def are_adjacent(self, src: int, dst: int) -> bool:
        """Returns True if src vertex has an outgoing edge that connects to dst vertex."""

        # Check if vertices are valid.
        if not self._is_valid_edge(src, dst):
            return False

        return self.adj_matrix[src][dst] > 0

    def neighbors(self, v: int) -> []:
        """Return all vertices that vertex v has an outgoing edge to."""

        neighbors: list = list()

        for i in range(self.v_count):
            if self.adj_matrix[v][i] > 0:
                neighbors.append(i)

        return neighbors

    def _is_valid_edge(self, src: int, dst: int) -> bool:
        """
        Returns True if an edge between a src and dst vertex is valid.

        An edge is invalid if the src and dst point to the same vertex, or if either vertex is not on the graph.
        """

        return src != dst and 0 <= src < self.v_count and 0 <= dst < self.v_count
