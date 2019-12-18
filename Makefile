
install:
	pip3 install -r requirements.txt
redis:
	docker run -d -p 6379:6379 redis:4-alpine
