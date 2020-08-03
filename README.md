# RESTful Wiki Entity Extractor
 
 
 ### Build the image
 
```bash
docker build . -t wiki:latest
```


## Enter the image for debugging
```bash
docker run -it -p 5000:5000 wiki 
conda activate entity-env
```

## Run the image
```bash
docker run -d -p 5000:5000 wiki
```

then navigate to `http://127.0.0.1:5000/`. The endpoint can be tested manually like,
```bash
http://127.0.0.1:5000/wiki-entities?data=https://en.wikipedia.org/wiki/Manhattan_Project
```

## Cleaning up
Containerized applications can take a lot of memory on your system. 
When you're done, use these optional cleanup steps.
````bash
# find the container ID in the list of running processes
docker ps
# kill the process
docker stop <container id>
# finally, delete the image
docker rmi wiki --force
```
 