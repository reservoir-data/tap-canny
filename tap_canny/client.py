"""REST client handling, including CannyStream base class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from singer_sdk import RESTStream
from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.pagination import BaseOffsetPaginator

if TYPE_CHECKING:
    from requests import Response
    from singer_sdk.helpers.types import Context


class CannyPaginator(BaseOffsetPaginator):
    """Canny API pagination strategy."""

    def has_more(self, response: Response) -> bool:
        """Return True if there are more pages to fetch.

        Args:
            response: The last response object.

        Returns:
            True if there are more pages to fetch.
        """
        data = response.json()
        return data.get("has_more", False)  # type: ignore[no-any-return]


class CannyStream(RESTStream[int]):
    """Canny stream class."""

    url_base = "https://canny.io/api"
    records_jsonpath = "$[*]"  # Or override `parse_response`.
    page_size = 100

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        api_key: str = self.config["api_key"]
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="apiKey",
            value=api_key,
            location="params",
        )

    @property
    def http_headers(self) -> dict[str, str]:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        return {"User-Agent": f"{self.tap_name}/{self._tap.plugin_version}"}

    def get_url_params(
        self,
        context: Context | None,  # noqa: ARG002
        next_page_token: int | None,  # noqa: ARG002
    ) -> dict[str, Any]:
        """Get URL query parameters.

        Args:
            context: Stream sync context.
            next_page_token: Next offset.

        Returns:
            Mapping of URL query parameters.
        """
        return {"limit": self.page_size}


class CannyOffsetStream(CannyStream):
    """Canny stream class with offset pagination."""

    def get_url_params(
        self,
        context: Context | None,
        next_page_token: int | None,
    ) -> dict[str, Any]:
        """Get URL query parameters."""
        params = super().get_url_params(context, next_page_token)
        params["skip"] = next_page_token or 0
        return params

    def get_new_paginator(self) -> CannyPaginator:
        """Get a new paginator instance.

        Returns:
            A new paginator instance.
        """
        return CannyPaginator(0, self.page_size)
