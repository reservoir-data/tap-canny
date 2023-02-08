# `tap-canny`

Singer tap for Canny.

Built with the [Meltano Singer SDK](https://sdk.meltano.com).

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
| users             | `/v1/users/list`      | FULL_TABLE         |
| votes             | `/v1/votes/list`      | FULL_TABLE         |

A full list of supported settings and capabilities is available by running: `tap-canny --about`

### Source Authentication and Authorization

- [ ] `Developer TODO:` If your tap requires special access on the source system, or any special authentication requirements, provide those here.

## Usage

You can easily run `tap-canny` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-canny --version
tap-canny --help
tap-canny --config CONFIG --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and then run:

```bash
poetry run pytest
```

You can also test the `tap-canny` CLI interface directly using `poetry run`:

```bash
poetry run tap-canny --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-canny
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-canny --version
# OR run a test `elt` pipeline:
meltano elt tap-canny target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
