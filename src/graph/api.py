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


def graph_api(loglevel: int):
    """Wrapper allowing :func: $(package) to be called with string
    arguments in a CLI fashion

    Args:
      loglevel: int
    """
    setup_logging(loglevel)
    _logger.info(f"Version: {__version__}")
    print("Running Graph")
    graph()
    _logger.info("Script ends here")


def graph():
    """
    Build graph
    """
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    s = 2
    d = 3

    # Function call
    print(g.countPaths(s, d))
