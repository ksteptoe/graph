# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from my_test_project.graph import graph`,
# when using this Python module as a library.

import logging
import sys

# from graph.Map import Map
import matplotlib.pyplot as plt
import networkx as nx

from graph import __version__

_logger = logging.getLogger(__name__)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def not_contiguous(node_set):
    sorted_list = sorted(node_set)
    for i in range(1, len(sorted_list)):
        if sorted_list[i] - sorted_list[i - 1] > 1:
            return False
    return True


def graph_api(the_map, start, dest, loglevel: int):
    """Wrapper allowing :func: $(package) to be called with string
    arguments in a CLI fashion

    Args:
      the_map: dict
      start: int
      dest: int
      loglevel: int
    """
    setup_logging(loglevel)
    _logger.info(f"Version: {__version__}")
    print("Running Graph")
    graph(the_map, start, dest)
    _logger.info("Script ends here")


def graph(the_map, start=0, dest=5):
    """
    Build graph
    """
    # node_set = {node for nodes in the_map for node in nodes}
    # assert not_contiguous(node_set)
    edges = [tuple(i) for i in the_map]
    G = nx.Graph(edges)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color="yellow")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=True)
    plt.draw()
    simple_paths = list(nx.all_simple_paths(G, source=start, target=dest))
    print(
        f"The number of simple paths between nodes {start} and {dest} "
        f"is {len(simple_paths)} and they are:"
    )
    for path in nx.all_simple_paths(G, source=start, target=dest):
        print(path)
    plt.show()
