

try:
    from gfg import loads, dumps
except ImportError:
    from .gfg import loads, dumps

__all__ = [loads, dumps]