FROM apache/airflow:2.8.0
COPY config_scripts/ config_scripts
COPY config_scripts/requirements.txt /requirements.txt

RUN pip install --user --upgrade pip
RUN pip install -r /requirements.txt
USER root
RUN apt-get update && \
    apt-get install -y vim && \
    apt-get install -y git && \
    apt-get install -y neovim

# Clean up APT when done to keep the image size small
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# RUN microdnf install -y dnf && \
#     dnf -y install yum && \
#     microdnf clean all
# RUN yum install pip
# RUN yum install git
