"""Canny tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_canny import streams


class TapCanny(Tap):
    """Singer tap for Canny."""

    name = "tap-canny"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="API Key for Canny",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Earliest datetime to get data from",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Canny streams.
        """
        return [
            streams.Boards(self),
            streams.Categories(self),
            streams.ChangelogEntries(self),
            streams.Comments(self),
            streams.Companies(self),
            streams.Opportunities(self),
            streams.Posts(self),
            streams.Tags(self),
            streams.Users(self),
            streams.Votes(self),
        ]
