from __future__ import annotations

import typing
import abc


_VALUE_TYPE = typing.TypeVar("_VALUE_TYPE")


class Query(abc.ABC):
    def get(self, key: str = None) -> typing.Optional