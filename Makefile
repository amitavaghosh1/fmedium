build:
	docker build -t fmedium .

run: build
	docker run -p 8741:8741 -d fmedium 
