# Setting up uv

To build uv project: `uv init {project_name}`

to sync dependencies: `uv sync`

## docker

Build image:
`docker build -t fastapi-app .`

Run image:
`docker run -p 8000:8000 fastapi-app`

## Check linting with ruff

`uvx ruff check {filename}`

to format with ruff:

`uvx ruff format {filename}`

## Testing

`uv run pytest`
