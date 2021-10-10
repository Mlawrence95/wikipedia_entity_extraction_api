FROM continuumio/miniconda3:4.7.12

COPY . /usr/REST_app/
WORKDIR /usr/REST_app

RUN conda update -n base -c defaults conda \
    && conda install -c conda-forge conda-lock -y \
    && conda config --add channels conda-forge \
    && conda-lock install --validate-platform=False -n myenv conda-linux-aarch64.lock  \
    && conda clean --all

WORKDIR /usr/REST_app/app

RUN echo "/opt/conda/bin/conda activate myenv" > ~/.bashrc

SHELL ["conda", "run", "-n", "entity-env", "/bin/bash", "-c"]

EXPOSE 5000

ENTRYPOINT python app.py
