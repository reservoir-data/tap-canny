"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from typing import Any

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_canny.tap import TapCanny

SAMPLE_CONFIG: dict[str, Any] = {}


TestTapCanny = get_tap_test_class(
    TapCanny,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(
        ignore_no_records_for_streams=[
            "comments",
            "companies",
            "opportunities",
        ],
    ),
)
