FROM continuumio/miniconda3:4.7.12

COPY . /usr/REST_app/

WORKDIR /usr/REST_app

RUN conda env create -f environment.yml

WORKDIR /usr/REST_app/app

RUN echo "/opt/conda/bin/conda activate myenv" > ~/.bashrc

SHELL ["conda", "run", "-n", "entity-env", "/bin/bash", "-c"]

EXPOSE 5000

ENTRYPOINT python app.py
