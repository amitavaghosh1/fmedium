FROM python:3.10.2

COPY . .

EXPOSE 8741

CMD ["./fmedium", "server"]
