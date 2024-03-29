"""
To install run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command $(package) inside your current environment.
"""

import logging

import click
import yaml

from graph.api import graph_api

__author__ = "Kevin Steptoe"
__copyright__ = "Kevin Steptoe"
__license__ = "MIT"

from graph import __version__

_logger = logging.getLogger(__name__)


@click.command()
@click.argument("the_map", type=click.Path(exists=True))
@click.option("-s", "--start", type=int, default=0)
@click.option("-d", "--destination", type=int, default=1)
@click.version_option(__version__, "--version")
@click.option("-v", "--verbose", "loglevel", type=int, flag_value=logging.INFO)
@click.option("-vv", "--very_verbose", "loglevel", type=int, flag_value=logging.DEBUG)
def cli(the_map, start, destination, loglevel):
    """Calls :func:`main` passing the CLI arguments extracted from click

    This function can be used as entry point to create console scripts with setuptools.
    """
    map_dic = []
    with open(the_map, "r") as stream:
        try:
            map_dic = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    graph_api(map_dic, start, destination, loglevel)


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run this Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m graph.graph 42
    #
    cli()
