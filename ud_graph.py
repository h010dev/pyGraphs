# Course: 
# Author: 
# Assignment: 
# Description:


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
        Add new vertex to the graph
        """
        pass
        
    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        pass

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        pass

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        pass

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        pass

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        pass
        
    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        pass
       
    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        pass
       
    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        pass

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """
        pass

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        pass
