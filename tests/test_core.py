"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from typing import Any

from singer_sdk.testing import get_tap_test_class

from tap_canny.tap import TapCanny

SAMPLE_CONFIG: dict[str, Any] = {}


TestTapCanny = get_tap_test_class(
    TapCanny,
    config=SAMPLE_CONFIG,
)
