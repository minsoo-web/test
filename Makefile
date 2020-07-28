install:
	npm install eslint

lint:
	eslint --ext .js -f checkstyle -o checkstyle-result.xml Rock-Paper-Scissors/
