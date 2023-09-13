"""
Defines common types to be used throughout the application
"""
from __future__ import annotations
import typing

T = typing.TypeVar("T")


class QueryProtocol(typing.Protocol):
    """
    Describes a type of object that can be used to read and write
    """
    def get(self, key: str = None, *, default: T = None) -> typing.Union[QueryProtocol, T, None]:
        """
        Get a value or node from the backing store

        @param key The key of the value to retrieve
        @param default The default value to retrieve if the value is not present

        @returns: Another object that may be queried, the found value, the default value, or none
        """
    
    def set(self, key: str, value: T) -> QueryProtocol:
        """
        Set a value to a key at the given node

        @param key: The key to map the value to
        @param value: The value to store
        """

