FROM continuumio/miniconda3

COPY . /usr/REST_app/

WORKDIR /usr/REST_app

RUN conda env create -f environment.yml

EXPOSE 5000

WORKDIR /usr/REST_app/app

ENTRYPOINT ["bash"]
