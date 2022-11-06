# test_fast_api
This is simple text searcher that using [elasticsearch](https://www.elastic.co/) and [PostgreSQL](https://www.postgresql.org/) as a db and [FastAPI](https://fastapi.tiangolo.com/) as an API framework.

# Installation
* First, you need to install latest version of language python on your computer.
You can download it [here](https://www.python.org/downloads/) or go to the Python official website - https://www.python.org/
* Second, you need to download the whole project to any directory on your computer.
* Third, you need to run file requirements.txt from your console. You need to go to the project directory and run this command
```
pip install -r requirements.txt
```
* Forth, you need to install elasticsearch engine. You can find simple guide how to do that [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).
Elasticsearch - https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
* Fifth, you need to install PostgreSQL database. You can do it by following this guide [here](https://www.postgresql.org/download/).
Or you can click on this link:) - https://www.postgresql.org/download/

Make sure that you install everything that needs to.

# Quick start
You need to configure connections to database and search engine. To do that, use file:
```
src/config/config.py
```

You can try this engine with example dataset.csv file. Or you can add your dataset, make sure that he has .csv format and dataset.csv name.
To do that run this in console.
```
python3 dataset_download.py
```
To run this program execute this command through your console.
```
python3 main.py
```

# Documentation
To find documentation and interact with API you can go to. 
```
http://host:port/docs
```
To get documentation in OpenAPI JSON format go to
```
http://host:port/docs/openapi.json
```

Enjoy:)
