# the house

A text-based game written in python

## Install or Download

- **Pip**: You can install the game with pip by typing `pip install thehouse`
- **Docker**: You can run the game directly using Docker:
  ```bash
  docker run -it dcdavidev/thehouse
  ```
- **Source**: You can download this repository and run it locally.

## Play

### Using Pip
If you have installed **thehouse** via pip, you can start the game by typing:
```bash
thehouse
```

### Using Docker
When running with Docker, ensure you use the `-it` flags to enable the interactive terminal required for the game:
```bash
docker run -it dcdavidev/thehouse
```

### From Source
If you downloaded the repository, ensure you have [Poetry](https://python-poetry.org/) installed, then run from the root of the repo:
```bash
poetry run python -m thehouse
```
