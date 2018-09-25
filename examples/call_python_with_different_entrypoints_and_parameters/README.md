
## Build container
```
docker build -t dockertest .
```

## Run container
```
docker run --rm -it dockertest python script.py --your-name <your_name>
```

Example
```
docker run --rm -it dockertest python script.py --your-name Peter
```
