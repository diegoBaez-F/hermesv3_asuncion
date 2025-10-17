""" Lint tests """
from pathlib import Path
import unittest

import pycodestyle  # formerly known as pep8


class TestLint(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP-8."""

        check_paths = [
            "hermesv3_bu",
            "tests",
        ]
        exclude_paths = [

        ]

        print("PEP8 check of directories: {}\n".format(", ".join(check_paths)))

        # Get paths wrt package root
        package_root = Path(__file__).resolve().parents[2]
        check_paths = [str(package_root / path) for path in check_paths]
        exclude_paths = [str(package_root / path) for path in exclude_paths]

        style = pycodestyle.StyleGuide()
        style.options.exclude = list(style.options.exclude) + exclude_paths
        style.options.max_line_length = 120

        self.assertEqual(style.check_files(check_paths).total_errors, 0)
