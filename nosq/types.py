"""
Defines common types to be used throughout the application
"""
from __future__ import annotations
import typing


VALID_VALUE_TYPE = typing.Union[
    None,
    str,
    int,
    float,
    bool,
    bytes,
    typing.Mapping,
    typing.Sequence
]

T = typing.TypeVar("T")


def is_valid_value(value: T) -> bool:
    """
    Determines if a given value may be stored 

    Args:
        value (T): _description_

    Returns:
        bool: _description_
    """
    if isinstance(value, typing.Mapping):
        for key, entry in value.items():
            if not isinstance(key, typing.Hashable):
                return False
            if not is_valid_value(entry):
                return False
        return True
    elif isinstance(value, typing.Sequence) and not isinstance(value, (str, bytes)):
        for entry in value:
            if not is_valid_value(entry):
                return False
        return True
    else:
        return isinstance(value, typing.get_args(VALID_VALUE_TYPE))


class QueryProtocol(typing.Protocol):
    """
    Describes a type of object that can be used to read and write
    """
    def get(self, default: T = None) -> typing.Optional[T]:
        """
        Gets the value of this current query item

        Args:
            default (T, optional): The default value to get if none was available. Defaults to None.

        Returns:
            typing.Optional[T]: The value at the given element
        """
    
    def set(self, key: typing.Hashable, value: VALID_VALUE_TYPE) -> QueryProtocol:
        """
        Set a value on the object

        Args:
            key (str): _description_
            value (T): _description_

        Returns:
            QueryProtocol: _description_
        """

    def find(self, *key: typing.Hashable) -> QueryProtocol:
        """
        Find elements based on path

        Returns:
            QueryProtocol: _description_
        """

    def is_empty(self) -> bool:
        """
        Whether there are any values

        Returns:
            bool: _description_
        """

    def keys(self) -> typing.Sequence[typing.Hashable]:
        """
        Get all keys on the current element

        Returns:
            typing.Sequence[typing.Hashable]: _description_
        """

    def values(self) -> typing.Sequence[VALID_VALUE_TYPE]:
        """
        Get all values on the current element

        Returns:
            typing.Sequence[VALID_VALUE_TYPE]: _description_
        """

    def items(self) -> typing.Sequence[typing.Tuple[typing.Hashable, VALID_VALUE_TYPE]]:
        """
        Get all keys and their corresponding values

        Returns:
            typing.Sequence[typing.Tuple[typing.Hashable, VALID_VALUE_TYPE]]: _description_
        """

