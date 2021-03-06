# Course: CS261 - Data Structures
# Author: Mohamed Al-Hussein
# Assignment: 06
# Description: Undirected graph implementation

from collections import deque


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph.

        If vertex with same name already exists, does nothing and returns to caller.
        """

        self.adj_list.setdefault(v, list())

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges.

        If vertex does not exist, does nothing and returns to caller.
        """

        # Remove vertex from adjacency list.
        v_edges: list = self.adj_list.pop(v, list())

        # Remove all edges incident to vertex.
        for edge in v_edges:
            self.adj_list[edge].remove(v)

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph between vertices u and v.

        If either vertex does not exist, creates them before adding edge.
        If edge already exists, or u and v refer to same vertex, does nothing and returns to caller.
        """

        # Add vertices to graph if they are missing.
        if u != v:
            self.add_vertex(u)
            self.add_vertex(v)

            # Add edge if vertices are not adjacent.
            if not self.are_adjacent(u, v):
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)

    def remove_edge(self, u: str, v: str) -> None:
        """
        Remove edge from the graph that is incident to vertices u and v.

        If either vertex does not exist, or there is no edge between them, does nothing and returns to caller.
        """

        if u != v and self.are_adjacent(u, v):
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)

    def get_vertices(self) -> []:
        """Return list of vertices in the graph in lexicographic order."""

        return sorted(list(self.adj_list.keys()))

    def get_edges(self) -> []:
        """
        Return list of edges in the graph in lexicographic order.

        Edges are returned as tuples of vertex endpoints.
        """

        edges: set = set()

        # Iterate through all vertices.
        for v in self.get_vertices():
            v_edges: list = list()

            # Add each vertex pair to edges.
            for u in self.adj_list[v]:

                # Only add vertex pair if it is unique (i.e. (u, v) != (v, u)).
                if (u, v) not in edges:
                    v_edges.append((v, u))

            edges.update(v_edges)

        return list(edges)

    def is_valid_path(self, path: []) -> bool:
        """
        Return True if the provided path is valid.

        An empty path or a path with a single vertex is considered valid.
        """

        # Check if path is empty or contains only a single vertex.
        if len(path) == 0:
            return True
        elif len(path) == 1:
            if path[0] in self.adj_list:
                return True
            else:
                return False

        # Iterate through vertices in path, checking if they are adjacent to each other so that they form a path.
        step: int = 0
        while step < len(path) - 1:
            u, v = path[step], path[step + 1]
            if not self.are_adjacent(u, v):
                return False

            step += 1

        return True

    def dfs(self, v_start: str, v_end: str = None) -> []:
        """
        Return list of vertices visited during DFS search from v_start vertex up to optional v_end vertex.

        If v_start is not in the graph, returns empty list.
        If v_end is not in the graph, will treat it as having no v_end parameter.

        Vertices are picked in ascending lexicographical order.
        """

        visited: list = list()

        # Check if v_start is in graph.
        if v_start not in self.adj_list:
            return visited

        # Check if v_end is in graph.
        if v_end not in self.adj_list:
            v_end = None

        # Traverse graph until we either reach v_end or traverse every vertex.
        vertices: deque = deque()
        vertices.appendleft(v_start)
        while len(vertices) > 0:
            v: str = vertices.popleft()
            if v not in visited:
                # Add vertex to visited vertices.
                visited.append(v)

                # Stop if vertex is equal to v_end.
                if v == v_end:
                    break

                # Add all neighbors of vertex in descending lexicographic order so that they are popped in ascending
                # lexicographic order.
                for neighbor in reversed(self.neighbors(v)):
                    vertices.appendleft(neighbor)

        return visited

    def bfs(self, v_start: int, v_end: int = None) -> []:
        """
        Return list of vertices visited during BFS search from v_start vertex up to optional v_end vertex.

        If v_start is not in the graph, returns empty list.
        If v_end is not in the graph, will treat it as having no v_end parameter.

        Vertices are picked in ascending lexicographical order.
        """

        visited: list = list()

        # Check if v_start is in graph.
        if v_start not in self.adj_list:
            return visited

        # Check if v_end is in graph.
        if v_end not in self.adj_list:
            v_end = None

        # Traverse graph until we either reach v_end or traverse every vertex.
        vertices: deque = deque()
        vertices.appendleft(v_start)
        while len(vertices) > 0:
            v: str = vertices.pop()
            if v not in visited:
                # Add vertex to visited vertices.
                visited.append(v)

                # Stop if vertex is equal to v_end.
                if v == v_end:
                    break

                # Add all neighbors of vertex in ascending lexicographic order.
                for neighbor in self.neighbors(v):
                    vertices.appendleft(neighbor)

        return visited

    def count_connected_components(self) -> int:
        """Return number of connected components in the graph."""

        return len(self.connected_components())

    def has_cycle(self):
        """Return True if graph contains a cycle."""

        # Iterate through all components in graph.
        components: list = self.connected_components()
        for component in components:

            # Perform DFS on each component, searching for any cycles.
            v_start: str = component.pop()
            visited: list = list()

            # Traverse all vertices in graph.
            vertices: deque = deque()
            vertices.appendleft(v_start)
            while len(vertices) > 0:
                v: str = vertices.popleft()
                if v not in visited:
                    # Add vertex to visited vertices.
                    visited.append(v)

                    # Add all neighbors of vertex in descending lexicographic order so that they are popped in ascending
                    # lexicographic order.
                    for neighbor in reversed(self.neighbors(v)):

                        # If neighbor already in vertices stack, then there's a cycle involving that neighbor.
                        if neighbor in vertices:
                            return True

                        vertices.appendleft(neighbor)

        return False

    def are_adjacent(self, u: str, v: str) -> bool:
        """Returns True if two vertices u and v are joined by an edge."""

        # Retrieve edges incident to vertices u and v.
        u_edges: list = self.adj_list.get(u, list())
        v_edges: list = self.adj_list.get(v, list())

        # Search for neighboring vertex inside shortest edge list to maintain O(min(deg(u), deg(v))) running time.
        return v in u_edges if self.degree(u) < self.degree(v) else u in v_edges

    def degree(self, v: str) -> int:
        """
        Returns the number of edges incident to a given vertex v.

        Returns -1 if vertex does not exist.
        """

        return len(self.adj_list.get(v, list())) if v in self.adj_list else -1

    def neighbors(self, v: str) -> []:
        """Return the neighbors of a vertex v in lexicographic order."""

        return sorted(self.adj_list.get(v, list()))

    def connected_components(self) -> []:
        """Return a list of list containing all connected components in DFS order."""

        components: list = list()

        # No vertices in graph.
        if self.is_empty():
            return components

        # Iterate through vertices, traversing from the start vertex using DFS order.
        rem_vertices: list = self.get_vertices()
        while len(rem_vertices) > 0:
            v_start: str = rem_vertices.pop()
            component: list = self.dfs(v_start)
            components.append(component)

            # Compute the set difference between remaining vertices and those just visited to determine if any
            # components remain that haven't been traversed.
            rem_vertices = list(set(rem_vertices) - set(component))

        return components

    def is_empty(self) -> bool:
        """Return True if graph contains no vertices."""

        return len(self.adj_list) == 0
