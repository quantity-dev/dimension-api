"""Dimension API."""

from typing import Final, Protocol, Self, runtime_checkable

__version__: Final = "0.0.1.dev0"
__all__ = ["__version__", "Dimension"]

@runtime_checkable
class Dimension(Protocol):
    def __mul__(self, other: Self, /) -> Self: ...
    def __truediv__(self, other: Self, /) -> Self: ...
    def __pow__(self, other: int, /) -> Self: ...
