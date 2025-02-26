<div align="center">

# tap-canny

<div>
  <a href="https://scientific-python.org/specs/spec-0000/">
    <img alt="SPEC 0 — Minimum Supported Dependencies" src="https://img.shields.io/badge/SPEC-0-green?labelColor=%23004811&color=%235CA038"/>
  </a>
  <a href="https://results.pre-commit.ci/latest/github/reservoir-data/tap-canny/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/reservoir-data/tap-canny/main.svg"/>
  </a>
  <a href="https://github.com/reservoir-data/tap-canny/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/reservoir-data/tap-canny"/>
  </a>
</div>

Singer tap for [Canny](https://canny.io/), a feedback management platform..

Built with the [Meltano Singer SDK](https://sdk.meltano.com).

</div>

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| api_key             | True     | None    | API Key for Canny |
| start_date          | False    | None    | Earliest datetime to get data from |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |

### Authentication

See the [Canny API docs](https://developers.canny.io/api-reference#authentication) for more information on how to authenticate with the Canny API.

## Supported Streams

| Stream            | Endpoint              | Replication Method |
| :---------------- | :-------------------- | :----------------- |
| boards            | `/v1/boards/list`     | FULL_TABLE         |
| categories        | `/v1/categories/list` | FULL_TABLE         |
| changelog_entries | `/v1/entries/list`    | FULL_TABLE         |
| comments          | `/v1/comments/list`   | FULL_TABLE         |
| companies         | `/v1/companies/list`  | FULL_TABLE         |
| opportunities     | `/v1/opportunities`   | FULL_TABLE         |
| posts             | `/v1/posts/list`      | FULL_TABLE         |
| tags              | `/v1/tags/list`       | FULL_TABLE         |
| users             | `/v2/users/list`      | FULL_TABLE         |
| votes             | `/v1/votes/list`      | FULL_TABLE         |

A full list of supported settings and capabilities is available by running: `tap-canny --about`

## Usage

You can easily run `tap-canny` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-canny --version
tap-canny --help
tap-canny --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
uv tool install --with tox-uv tox
```

### Create and Run Tests

Run all tests:

```bash
tox run-parallel
```

You can also test the `tap-canny` CLI interface directly:

```bash
hatch run sync:console -- --about --format=json
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Go ahead and [install Meltano](https://docs.meltano.com/getting-started/installation/) if you haven't already.

1. Install all plugins

   ```bash
   meltano install
   ```

1. Check that the extractor is working properly

   ```bash
   meltano invoke tap-canny --version
   ```

1. Execute an ELT pipeline

   ```bash
   meltano run tap-canny target-jsonl
   ```
