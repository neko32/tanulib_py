from abc import ABC, abstractmethod
from typing import TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')

class CacheTrait(ABC):
    """
    Provide cache feature
    """

    @abstractmethod
    def add(self, key:K, value:V) -> None:
        """Add value with key to a cache"""
        pass

    @abstractmethod
    def get(self, key:K, default_v:Optional[K]) -> Optional[V]:
        """get value with key from a cache"""
        pass

    @abstractmethod
    def evict(self, key:K, value:V) -> Optional[V]:
        """Remove value for the specified key from a cache"""
        pass

    @abstractmethod
    def size(self) -> int:
        """Return number of items in cache"""
        pass

class InMemCache(CacheTrait):
    """
    Provide cache feature using in memory cache
    """

    def __init__(self):
        self.cache = {}

    def add(self, key:K, value:V) -> None:
        """Add value with key to an in memory cache"""
        if key not in self.cache:
            self.cache[key] = value

    def get(self, key:K, default_v:Optional[K]) -> Optional[V]:
        """get value with key from an in memory cache"""
        if key not in self.cache:
            if default_v is not None:
                return default_v
            else:
                return None
        else:
            return self.cache[key]

    def evict(self, key:K) -> Optional[V]:
        """Remove value for the specified key from an in memory cache"""
        if key not in self.cache:
            return None
        else:
            return self.cache.pop(key)

    def size(self) -> int:
        """Return number of items in cache"""
        return len(self.cache)

    def __repr__(self) -> str:
        return self.cache.__repr__()