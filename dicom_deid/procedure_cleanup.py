from collections import defaultdict


def find_redundant_nodes(edges, breaking_nodes):
    """
    Finds dead weight by filtering for nodes which are redundant.

    A node is useless if all the paths to it from the root have
    breaking nodes.

    Args:
        edges: List of dicts with 'path' key in format 'module:parent:child'
        breaking_nodes: Set of node IDs that break

    Returns:
        Set of nodes that are redudendant
    """

    # Collect all the possible paths for a node
    node_to_paths = defaultdict(lambda: [])
    for edge in edges:
        path = edge["path"].split(":")

        node = path[-1]

        # Skip the module and actual node definition
        path = path[1:-1]

        node_to_paths[node].append(path)

    redudendants = set()
    for node, paths in node_to_paths.items():
        # Check if there is a break in the path
        if all(set(path) & breaking_nodes for path in paths):
            redudendants.add(node)

    return redudendants
