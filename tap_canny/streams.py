"""Stream type classes for tap-canny."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, override

from singer_sdk import typing as th
from singer_sdk.pagination import BaseAPIPaginator

from tap_canny.client import CannyStream

if TYPE_CHECKING:
    from requests import Response
    from singer_sdk.helpers.types import Context, Record


class Boards(CannyStream):
    """Boards stream."""

    name = "boards"
    path = "/v1/boards/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.boards[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The board's system ID",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the board was created",
        ),
        th.Property(
            "isPrivate",
            th.BooleanType,
            description="Whether the board is private or not",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The board's name",
        ),
        th.Property(
            "postCount",
            th.IntegerType,
            description="The number of posts on the board",
        ),
        th.Property(
            "privateComments",
            th.BooleanType,
            description="Whether the board allows private comments or not",
        ),
        th.Property(
            "token",
            th.StringType,
            description="The board's token",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The board's URL",
        ),
    ).to_dict()


class Categories(CannyStream):
    """Categories stream."""

    name = "categories"
    path = "/v1/categories/list"
    primary_keys: ClassVar[list[str]] = ["id"]
    records_jsonpath = "$.categories[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The category's system ID",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the category was created",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The category's name",
        ),
        th.Property(
            "parentID",
            th.IntegerType,
            description="The category's parent ID",
        ),
        th.Property(
            "postCount",
            th.IntegerType,
            description="The number of posts in the category",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The category's URL",
        ),
    ).to_dict()


class ChangelogEntries(CannyStream):
    """Changelog entries stream."""

    name = "changelog_entries"
    path = "/v1/entries/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.entries[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The entry's system ID",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the entry was created",
        ),
        th.Property(
            "labels",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "id",
                        th.StringType,
                        description="The label's system ID",
                    ),
                    th.Property(
                        "created",
                        th.DateTimeType,
                        description="The date and time the label was created",
                    ),
                    th.Property(
                        "entryCount",
                        th.IntegerType,
                        description="The number of entries with the label",
                    ),
                    th.Property(
                        "name",
                        th.StringType,
                        description="The label's name",
                    ),
                    th.Property(
                        "url",
                        th.StringType,
                        description="The label's URL",
                    ),
                ),
            ),
            description="The entry's description",
        ),
        th.Property(
            "lastSaved",
            th.DateTimeType,
            description="The date and time the entry was last saved",
        ),
        th.Property(
            "markdownDetails",
            th.StringType,
            description="The entry's markdown details",
        ),
        th.Property(
            "plaintextDetails",
            th.StringType,
            description="The entry's plaintext details",
        ),
        th.Property(
            "posts",
            th.ArrayType(th.ObjectType()),
            description="The entry's posts",
        ),
        th.Property(
            "publishedAt",
            th.DateTimeType,
            description="The date and time the entry was published",
        ),
        th.Property(
            "reactions",
            th.ObjectType(),
            description="The entry's reactions",
        ),
        th.Property(
            "scheduledFor",
            th.DateTimeType,
            description="The date and time the entry is scheduled for",
        ),
        th.Property(
            "status",
            th.StringType,
            description="The entry's status",
        ),
        th.Property(
            "title",
            th.StringType,
            description="The entry's title",
        ),
        th.Property(
            "types",
            th.ArrayType(th.StringType),
            description="The entry's types",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The entry's URL",
        ),
    ).to_dict()


class Comments(CannyStream):
    """Comments stream."""

    name = "comments"
    path = "/v1/comments/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.comments[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The comment's system ID",
        ),
        th.Property(
            "author_id",
            th.StringType,
            description="The comment's author ID",
        ),
        th.Property(
            "board_id",
            th.StringType,
            description="The comment's board ID",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the comment was created",
        ),
        th.Property(
            "imageURLs",
            th.ArrayType(th.StringType),
            description="The comment's image URLs",
        ),
        th.Property(
            "internal",
            th.BooleanType,
            description="Whether the comment is internal or not",
        ),
        th.Property(
            "likeCount",
            th.IntegerType,
            description="The number of likes on the comment",
        ),
        th.Property(
            "mentions",
            th.ArrayType(th.StringType),
            description="The comment's mentions",
        ),
        th.Property(
            "parentID",
            th.StringType,
            description="The comment's parent ID",
        ),
        th.Property(
            "post_id",
            th.StringType,
            description="The comment's post ID",
        ),
        th.Property(
            "private",
            th.BooleanType,
            description="Whether the comment is private or not",
        ),
        th.Property(
            "reactions",
            th.ObjectType(),
            description="The comment's reactions",
        ),
        th.Property(
            "value",
            th.StringType,
            description="The comment text",
        ),
    ).to_dict()

    @override
    def post_process(
        self,
        row: Record,
        context: Context | None = None,
    ) -> Record | None:
        """Post-process a row."""
        author = row.pop("author", {})
        board = row.pop("board", {})
        mentions = row.pop("mentions", [])
        post = row.pop("post", {})

        row["author_id"] = author.get("id")
        row["board_id"] = board.get("id")
        row["mentions"] = [mention.get("id") for mention in mentions]
        row["post_id"] = post.get("id")

        return row


class Companies(CannyStream):
    """Companies stream."""

    name = "companies"
    path = "/v1/companies/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.companies[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The company's system ID",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the company was created",
        ),
        th.Property(
            "customFields",
            th.ArrayType(th.ObjectType()),
            description="The company's custom fields",
        ),
        th.Property(
            "domain",
            th.StringType,
            description="The company's domain",
        ),
        th.Property(
            "memberCount",
            th.IntegerType,
            description="The number of members in the company",
        ),
        th.Property(
            "monthlySpend",
            th.NumberType,
            description="The company's monthly spend",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The company's name",
        ),
    ).to_dict()


class Opportunities(CannyStream):
    """Opportunities stream."""

    name = "opportunities"
    path = "/v1/opportunities/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.opportunities[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The opportunity's system ID",
        ),
        th.Property(
            "closed",
            th.BooleanType,
            description="Whether the opportunity is closed or not",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The opportunity's name",
        ),
        th.Property(
            "postIDs",
            th.ArrayType(th.StringType),
            description="The opportunity's post IDs",
        ),
        th.Property(
            "salesforceOpportunityID",
            th.StringType,
            description="The opportunity's Salesforce opportunity ID",
        ),
        th.Property(
            "value",
            th.NumberType,
            description="The opportunity's value",
        ),
        th.Property(
            "won",
            th.BooleanType,
            description="Whether the opportunity is won or not",
        ),
    ).to_dict()


class Posts(CannyStream):
    """Posts stream."""

    name = "posts"
    path = "/v1/posts/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.posts[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The post's system ID",
        ),
        th.Property(
            "author_id",
            th.StringType,
            description=(
                "The user who authored the post. If the author's account has been "
                "deleted, this field will be null"
            ),
        ),
        th.Property(
            "board_id",
            th.StringType,
            description="The board this post is associated with",
        ),
        th.Property(
            "by",
            th.StringType,
            description="The user who created the post on behalf of the author",
        ),
        th.Property(
            "category_id",
            th.StringType,
            description="The user who created the post on behalf of the author",
        ),
        th.Property(
            "commentCount",
            th.IntegerType,
            description="The number of comments on the post",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the post was created",
        ),
        th.Property(
            "customFields",
            th.ArrayType(th.ObjectType()),
            description="The post's custom fields",
        ),
        th.Property(
            "details",
            th.StringType,
            description=(
                "Any details the user included in the post. This is the longer text "
                'field (where the shorter one is "title")'
            ),
        ),
        th.Property(
            "eta",
            th.StringType,
            description="The month and year the post is estimated to be delivered",
        ),
        th.Property(
            "imageURLs",
            th.ArrayType(th.StringType),
            description="An array of the URLs of the images associated with this post",
        ),
        th.Property(
            "owner_id",
            th.StringType,
            description="The owner of the post",
        ),
        th.Property(
            "score",
            th.IntegerType,
            description="The number of votes that have been cast on this post",
        ),
        th.Property(
            "status",
            th.StringType,
            description=(
                'The post\'s status: "open", "under review", "planned", '
                '"in progress", "complete", "closed", or any other status your '
                "team has set on the settings page."
            ),
        ),
        th.Property(
            "statusChangedAt",
            th.DateTimeType,
            description="The date and time the post's status was last changed",
        ),
        th.Property(
            "tags",
            th.ArrayType(th.StringType),
            description="An array of the tags associated with this post",
        ),
        th.Property(
            "title",
            th.StringType,
            description="The post's title",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The post's URL",
        ),
    ).to_dict()

    @override
    def post_process(
        self,
        row: Record,
        context: Context | None = None,
    ) -> Record | None:
        """Post-process a record."""
        author = row.pop("author", {}) or {}
        board = row.pop("board", {}) or {}
        by = row.pop("by", {}) or {}
        category = row.pop("category", {}) or {}
        owner = row.pop("owner", {}) or {}

        row["author_id"] = author.get("id")
        row["board_id"] = board.get("id")
        row["by"] = by.get("id")
        row["category_id"] = category.get("id")
        row["owner_id"] = owner.get("id")

        return row


class StatusChanges(CannyStream):
    """Status changes stream."""

    name = "status_changes"
    path = "/v1/status_changes/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.statusChanges[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The status change's system ID",
        ),
        th.Property(
            "changeComment",
            th.ObjectType(
                th.Property(
                    "value",
                    th.StringType,
                ),
                th.Property(
                    "imageURLs",
                    th.ArrayType(th.StringType),
                ),
            ),
            description="The status change's comment",
        ),
        th.Property(
            "changer_id",
            th.StringType,
            description="The status change's changer",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the status change was created",
        ),
        th.Property(
            "post_id",
            th.StringType,
            description="The status change's post",
        ),
        th.Property(
            "status",
            th.StringType,
            description="The status the post was changed to",
        ),
    ).to_dict()

    @override
    def post_process(
        self,
        row: Record,
        context: Context | None = None,
    ) -> Record | None:
        """Post process the row."""
        changer = row.pop("changer", {})
        post = row.pop("post", {})

        row["changer_id"] = changer.get("id")
        row["post_id"] = post.get("id")

        return row


class Tags(CannyStream):
    """Tags stream."""

    name = "tags"
    path = "/v1/tags/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.tags[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The tag's system ID",
        ),
        th.Property(
            "board_id",
            th.StringType,
            description="The tag's board ID",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the tag was created",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The tag's name",
        ),
        th.Property(
            "postCount",
            th.IntegerType,
            description="The number of posts with the tag",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The tag's URL",
        ),
    ).to_dict()

    @override
    def post_process(
        self,
        row: Record,
        context: Context | None = None,
    ) -> Record | None:
        """Post process the row."""
        board = row.pop("board", {})

        row["board_id"] = board.get("id")

        return row


class UsersPaginator(BaseAPIPaginator[str | None]):
    """Users paginator."""

    @override
    def has_more(self, response: Response) -> bool:
        """Return True if there are more pages to fetch."""
        data = response.json()
        return data.get("hasNextPage", False)  # type: ignore[no-any-return]

    @override
    def get_next(self, response: Response) -> str | None:
        """Check if there are more pages."""
        data = response.json()
        return data.get("cursor")  # type: ignore[no-any-return]


class Users(CannyStream):
    """Users stream."""

    name = "users"
    path = "/v2/users/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.users[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The user's system ID",
        ),
        th.Property(
            "alias",
            th.StringType,
            description="The user's alias",
        ),
        th.Property(
            "avatarURL",
            th.StringType,
            description="The user's avatar URL",
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the user was created",
        ),
        th.Property(
            "customFields",
            th.ArrayType(th.ObjectType()),
            description="The user's custom fields",
        ),
        th.Property(
            "email",
            th.StringType,
            description="The user's email",
        ),
        th.Property(
            "isAdmin",
            th.BooleanType,
            description="Whether the user is an admin or not",
        ),
        th.Property(
            "lastActivity",
            th.DateTimeType,
            description="The date and time of the user's last activity",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The user's name",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The user's URL",
        ),
        th.Property(
            "userID",
            th.StringType,
            description=(
                "The user's unique identifier in your application. This field can be "
                "null. We only have this data if the user was authenticated via single "
                "sign-on, or if it was added via API."
            ),
        ),
    ).to_dict()

    @override
    def get_new_paginator(self) -> UsersPaginator:
        """Get a new paginator."""
        return UsersPaginator(None)


class Votes(CannyStream):
    """Votes stream."""

    name = "votes"
    path = "/v1/votes/list"
    primary_keys: tuple[str, ...] = ("id",)
    records_jsonpath = "$.votes[*]"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The vote's system ID",
        ),
        th.Property(
            "board_id",
            th.StringType,
            description="The vote's board ID",
        ),
        th.Property(
            "by",
            th.StringType,
            description=(
                "The admin who cast this vote on behalf of a user. If the user voted "
                "themselves, this field will be null."
            ),
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="The date and time the vote was created",
        ),
        th.Property(
            "post_id",
            th.StringType,
            description="The vote's post ID",
        ),
        th.Property(
            "voter_id",
            th.StringType,
            description="The vote's voter ID",
        ),
    ).to_dict()

    @override
    def post_process(
        self,
        row: dict[str, Any],
        context: Context | None = None,
    ) -> dict[str, Any] | None:
        """Post process the row."""
        board = row.pop("board", {})
        post = row.pop("post", {})
        voter = row.pop("voter", {})

        row["board_id"] = board.get("id")
        row["post_id"] = post.get("id")
        row["voter_id"] = voter.get("id")

        return row
