from collections import defaultdict

from dicom_deid.models import ActionChoices

BREAKING_ACTIONS = (
    ActionChoices.REMOVE,
    ActionChoices.REPLACE,
    ActionChoices.REPLACE_0,
    ActionChoices.REJECT,
)


def find_unreachable_nodes(edges, breaking_nodes):
    """
    Finds dead weight by filtering for nodes which are redundant.

    A node is unreachable if all the paths to it from the root have
    breaking nodes.

    Args:
        edges: List of lists, where each inner list is the full path
        [parent1, ..., node] breaking_nodes: Set of node IDs that break

    Returns:
        Set of nodes that are unreachable
    """

    # Collect all the possible paths per node
    node_to_paths = defaultdict(list)
    for edge in edges:
        node = edge[-1]

        # Skip the actual node definition
        path = edge[:-1]

        node_to_paths[node].append(path)

    unreachable_nodes = set()
    for node, paths in node_to_paths.items():
        # Check if there is a break in the path
        if all(set(path) & breaking_nodes for path in paths):
            unreachable_nodes.add(node)

    return unreachable_nodes


def remove_unreachable_actions(procedure, dicom_standard):
    """
    Redundant actions are actions that, because of the actions set for their parent
    sequences have no effect.

    For instance, under sequence A a tag 0000,0000 might have action 'U'. However,
    if sequence A has action 'X', the action for tag 0000,0000 is redundant.

    However, if another sequence B also uses tag 0000,0000 the tag action is NOT
    redundant. Unless sequence B is also removed (or replaced)!
    """
    for sop_id in procedure.sop_ids:

        actions = procedure.get_sop_actions(sop_id)
        breaking_nodes = set()
        for tag, action in actions.items():
            if action and action["default"] in BREAKING_ACTIONS:
                breaking_nodes.add(tag)

        edges = dicom_standard.get_all_attribute_paths_via_sop(sop_id=sop_id)

        redundant_tags = find_unreachable_nodes(
            edges=edges, breaking_nodes=breaking_nodes
        )

        for tag in redundant_tags:
            procedure.remove_action(sop_id, tag=tag)

    return procedure
