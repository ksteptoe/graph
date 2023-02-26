# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from my_test_project.graph import graph`,
# when using this Python module as a library.

import logging
import sys

from graph import __version__
from graph.Graph import Graph

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


def not_contiguous(lst):
    lst.sort()
    for i in range(1, len(lst)):
        if list[i] - list[i - 1] > 1:
            return False
    return True


def graph_api(the_map, loglevel: int):
    """Wrapper allowing :func: $(package) to be called with string
    arguments in a CLI fashion

    Args:
      the_map: dict
      loglevel: int
    """
    setup_logging(loglevel)
    _logger.info(f"Version: {__version__}")
    print("Running Graph")
    graph(the_map)
    _logger.info("Script ends here")


def graph(the_map):
    """
    Build graph
    """
    node_set = {node for nodes in the_map for node in nodes}
    assert not_contiguous(node_set)
    node_tuples = [tuple(i) for i in the_map]
    g = Graph(len(node_set))
    for edge1, edge2 in node_tuples:
        g.addEdge(edge1, edge2)
    start = 2
    destination = 3

    # Calculate the number of paths with CountPaths
    print(
        f"The number of routes through the park are {g.countPaths(start, destination)}"
    )
