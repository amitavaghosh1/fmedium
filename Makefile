build:
	docker build -t fmedium .

run: build
	docker run -d -p 8741:8741 -it fmedium 
