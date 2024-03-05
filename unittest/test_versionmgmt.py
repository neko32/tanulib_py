from unittest import TestCase, main
from tlib.core.version_mgmt import *


class VersionMgmtTest(TestCase):

    def test_semverinfo(self):
        major = 3
        minor = 12
        patch = 5
        semver = from_semverint_to_semverinfo(major, minor, patch)
        self.assertEqual(semver.major, major)
        self.assertEqual(semver.minor, minor)
        self.assertEqual(semver.patch, patch)
        mmp = f"{major}.{minor}.{patch}"
        semver2 = SemVerInfo(mmp)
        self.assertEqual(semver2.major, major)
        self.assertEqual(semver2.minor, minor)
        self.assertEqual(semver2.patch, patch)

    def test_semver_comparison(self):
        left = SemVerInfo("1.2.15")
        right_smaller_by_major = SemVerInfo("0.9.20")
        right_smaller_by_minor = SemVerInfo("1.1.112")
        right_smaller_by_patch = SemVerInfo("1.2.14")
        right_tie = SemVerInfo("1.2.15")
        right_bigger_by_major = SemVerInfo("2.0.0")
        right_bigger_by_minor = SemVerInfo("1.7.10")
        right_bigger_by_patch = SemVerInfo("1.2.21")
        self.assertEqual(left.compare(right_smaller_by_major),
                         ComparisonResult.LEFT_BIGGER)
        self.assertEqual(left.compare(right_smaller_by_minor),
                         ComparisonResult.LEFT_BIGGER)
        self.assertEqual(left.compare(right_smaller_by_patch),
                         ComparisonResult.LEFT_BIGGER)
        self.assertEqual(left.compare(right_tie), ComparisonResult.BOTH_EQUAL)
        self.assertEqual(left.compare(right_bigger_by_major),
                         ComparisonResult.LEFT_SMALLER)
        self.assertEqual(left.compare(right_bigger_by_minor),
                         ComparisonResult.LEFT_SMALLER)
        self.assertEqual(left.compare(right_bigger_by_patch),
                         ComparisonResult.LEFT_SMALLER)

    def test_latest_version_fetch(self):
        git_ver_chk = GithubReleaseLatestVersion("sfackler", "rust-openssl")
        result = git_ver_chk.fetch_retrieve_version()
        self.assertTrue(result.startswith("openssl"))

    def test_fetch_failure(self):
        git_ver_chk = GithubReleaseLatestVersion("sonnano", "sonzaishineyo")
        with self.assertRaises(Exception):
            git_ver_chk.fetch_retrieve_version()

    def test_version_comparator(self):
        git_ver_chk = GithubReleaseLatestVersion("sfackler", "rust-openssl")
        obvious_prev_ver = "openssl-v0.0.0"
        obvious_fut_ver = "openssl-v100.0.0"
        version_from_git = git_ver_chk.fetch_retrieve_version()
        print(f"fetched latest ver is {git_ver_chk.latest_version_cache}")
        comparator = RustOpenSSLVersionComparator(
            obvious_prev_ver, version_from_git)
        self.assertTrue(comparator.is_more_latest_version_available())
        comparator = RustOpenSSLVersionComparator(
            obvious_fut_ver, version_from_git)
        self.assertFalse(comparator.is_more_latest_version_available())


if __name__ == "__main__":
    main()
