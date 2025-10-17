# coding=utf-8
"""Script to run the tests for HERMESv3_BU and generate the code coverage report"""

from pathlib import Path

import os
import sys

import pytest


work_path = Path(__file__).resolve().parent
os.chdir(work_path)
print(work_path)


version = sys.version_info[0]
report_dir = Path("tests") / "report" / f"python{version}"
report_dir.mkdir(parents=True, exist_ok=True)
html_report_dir = report_dir / "coverage_html"
xml_report_path = report_dir / "coverage.xml"
errno = pytest.main([
    "tests",
    "--ignore=tests/report",
    "--cov=hermesv3_bu",
    "--cov-report=term",
    f"--cov-report=html:{html_report_dir}",
    f"--cov-report=xml:{xml_report_path}",
])
sys.exit(errno)
