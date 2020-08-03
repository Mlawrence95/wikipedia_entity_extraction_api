# RESTful Wiki Entity Extractor

 A simple Flask REST API for extracting entities from wikipedia pages. Useful for constructing knowledge graphs over a set of wikipedia pages. 

This app expects a GET request looking like:
```json
{
    "data": "https://en.wikipedia.org/wiki/Manhattan_Project"
}
```

To the endpoint `/wiki-entities`. It returns a response with the (rough) schema:
```json
{"response_data": 
	{
	"entities": ["The Manhattan Project", "World War II", "first", "the United States", "the United Kingdom", "Canada", "From 1942 to 1946", "Leslie Groves",
		"the U.S. Army Corps of Engineers", "Robert Oppenheimer", "the Los Alamos Laboratory", "Army", "Manhattan", "Manhattan", "Development of Substitute ", 
		"September 1946", "Their Nuclear Energy for the Propulsion of Aircraft", "the immediate postwar years", "mid-1946", "Oak Ridge", "the Atomic Energy Commission", 
		"Groves", "the Manhattan Project", "Five years ago", "Atomic Power", "American", "2014", "the United States Congress", "the Manhattan Project", 
		"The Manhattan Project National Historical Park", "10 November 2015"], 

	"ent_types": ["ORG", "EVENT", "ORDINAL", "GPE", "GPE", "GPE", "DATE", "PERSON", "ORG", "PERSON", "ORG", "ORG", "GPE", "GPE", "ORG", "NORP", "PERSON", "ORG", "DATE", 
		"CARDINAL", "MONEY", "MONEY", "DATE", "PERCENT", "PERCENT", "CARDINAL", "GPE", "GPE", "GPE", "CARDINAL", "PERSON", "ORG", "PERCENT", "GPE", "GPE", "GPE", "ORG", 
		"ORG", "ORG", "ORG", "ORG", "ORG", "CARDINAL", "ORG", "ORG", "GPE", "GPE", "ORG", "GPE", "GPE", "ORG", "MONEY", "DATE", "PERSON", "ORG", "PERSON", "ORG", "DATE", 
		"ORG", "ORG", "ORG", "ORG", "LOC", "PERSON", "ORG", "FAC", "DATE", "ORG", "DATE", "DATE", "PERSON", "ORG", "ORG", "ORG", "DATE", "ORG", "NORP", "DATE", "ORG", "ORG", "ORG", "DATE"]
		}
	}
```

(This is a fake example)


# To use the app, you have two options: Source or Docker


## 1) Source
Having `conda` installed on your machine, you can run `conda env create -f environment.yml` in this repo. From there, activate your environment with `conda activate entity-env`. In the environment, cd into `app/`, and then run `python app.py`. Ta-da! Your app should now be running on localhost on port 5000. Feel free to change the port in `app.py`.




## 2) Docker 
Docker is slightly more involved, though not difficult. 

### Build the image
 
```bash
docker build . -t wiki:latest
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
```bash
# find the container ID in the list of running processes
docker ps
# kill the process
docker stop <container id>
# finally, delete the image
docker rmi wiki --force
```

## Enter the image for debugging
```bash
docker run -it -p 5000:5000 wiki 
conda activate entity-env
```



##### Thanks for reading! Please feel free to raise any issues or submit a PR for enhancements.