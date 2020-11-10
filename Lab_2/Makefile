all: install test run deploy

install:
	echo "Installing pipenv and dependencies..."
	pip3 install pipenv
	pipenv --python 3.6
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	echo "Tests starts..."
	pipenv run pytest tests/tests.py >> results.txt

run:
	echo "Run app..."
	pipenv run python3 app.py >> results.txt

deploy:
	echo "Commit results.txt to git."
	git add .
	git commit -m "Update result.txt"
	git push origin main 
