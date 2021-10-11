FROM continuumio/miniconda3:4.7.12

COPY . /usr/REST_app/
WORKDIR /usr/REST_app

ENV LOCAL_LOCKFILE=conda-linux-64.lock
ENV ARM_LOCKFILE=conda-linux-aarch64.lock

RUN conda update -n base -c defaults conda \
    && conda install -c conda-forge conda-lock -y \
    && conda config --add channels conda-forge \
    && conda create --name entity-env --file $ARM_LOCKFILE \
    && conda clean --all

WORKDIR /usr/REST_app/app

RUN echo "/opt/conda/bin/conda activate myenv" > ~/.bashrc

SHELL ["conda", "run", "-n", "entity-env", "/bin/bash", "-c"]

EXPOSE 5000

ENTRYPOINT python app.py
