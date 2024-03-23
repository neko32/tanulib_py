from abc import ABC, abstractmethod
from typing import TypeVar, Optional
from enum import Enum, auto
import requests

T = TypeVar('T')


class ComparisonResult(Enum):
    """
    Comparison Result
    """
    LEFT_SMALLER = auto()
    BOTH_EQUAL = auto()
    LEFT_BIGGER = auto()


class SemVerInfo:
    """
    Parse and store SemVer version data
    """

    def __init__(self, semver: str) -> None:
        """Parse and store sevmer data"""
        vers = semver.split(".")
        self._major = int(vers[0])
        self._minor = int(vers[1])
        self._patch = int(vers[2])

    def compare(self, another: 'SemVerInfo') -> ComparisonResult:
        """compare with another semver"""
        # major version check
        if self.major > another.major:
            return ComparisonResult.LEFT_BIGGER
        elif self.major < another.major:
            return ComparisonResult.LEFT_SMALLER
        # if major is tie, then check minor
        if self.minor > another.minor:
            return ComparisonResult.LEFT_BIGGER
        elif self.minor < another.minor:
            return ComparisonResult.LEFT_SMALLER
        # if minor is also tie, then last check patch
        if self.patch > another.patch:
            return ComparisonResult.LEFT_BIGGER
        elif self.patch < another.patch:
            return ComparisonResult.LEFT_SMALLER
        else:
            return ComparisonResult.BOTH_EQUAL

    @property
    def major(self) -> int:
        return self._major

    @property
    def minor(self) -> int:
        return self._minor

    @property
    def patch(self) -> int:
        return self._patch


def from_semverint_to_semverinfo(major: int, minor: int, patch: int) -> SemVerInfo:
    """derive Semver from major, minor, patch integers"""
    return SemVerInfo(f"{major}.{minor}.{patch}")


class VersionComparator(ABC):
    """Version Comparator abstract class"""

    def __init__(self, current_version: T, new_version: T) -> None:
        self.current_version = current_version
        self.new_version = new_version

    @abstractmethod
    def is_more_latest_version_available(self) -> bool:
        pass


class RustOpenSSLVersionComparator(VersionComparator):
    """A sample version comparator for Rust's OpenSSL lib"""

    def _extract_version(self, tag_name: str) -> SemVerInfo:
        """extract version from tag"""
        v_idx = tag_name.index('v')
        semver = tag_name[v_idx + 1:]
        return SemVerInfo(semver)

    def is_more_latest_version_available(self) -> bool:
        """check whether more latest version is available or not"""
        current_semver = self._extract_version(self.current_version)
        new_semver = self._extract_version(self.new_version)
        comp = current_semver.compare(new_semver)
        return False if comp == ComparisonResult.LEFT_BIGGER \
            or comp == ComparisonResult.BOTH_EQUAL else True


class LatestVersionFetch(ABC):
    """provide a logic to fetch the latest version"""

    @abstractmethod
    def fetch_retrieve_version(self) -> T:
        pass


class GithubReleaseLatestVersion(LatestVersionFetch):
    """Provide logic to fetch the latest version from Github"""

    def __init__(self, owner: str, repo: str) -> None:
        """Set repos and owner to get the latest version"""
        self.repo = repo
        self.owner = owner
        self.fetched_latestion_version = None

    def fetch_retrieve_version(self) -> T:
        """fetch latest version available"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
        resp = requests.get(
            url=url,
            headers={'Accept': 'application/vnd.github+json'}
        )
        if resp.status_code != 200:
            raise Exception(f"failed to access to the site - {url}")
        resp_json = resp.json()
        self.fetched_latestion_version = resp_json['tag_name']
        return resp_json['tag_name']

    @property
    def latest_version_cache(self) -> Optional[str]:
        """get latest version from cache"""
        return self.fetched_latestion_version
