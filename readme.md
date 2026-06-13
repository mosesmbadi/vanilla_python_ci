uvicorn main:app --reload


docker build -t mosesmbadi/vanilla_client:latest .
docker push mosesmbadi/vanilla_client:latest


docker run -d -p 3000:3000 --name vanilla_client mosesmbadi/vanilla_client:latest

docker push mosesmbadi/vanilla_client:latest