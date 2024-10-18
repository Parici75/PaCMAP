from importlib.metadata import version

from .pacmap import PaCMAP

__version__ = version("pacmap")
__all__ = ["PaCMAP"]
