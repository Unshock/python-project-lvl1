#Makefile

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

brain-games:
	poetry run brain_games

lint:
	poetry run flake8 brain_games
