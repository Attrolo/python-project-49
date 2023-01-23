install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games

make lint:
	poetry run flake8 brain_games

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

setup:
	poetry install
	poetry build
	poetry publish
	package-install
