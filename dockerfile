# actions used
FROM bitnami/pytorch
USER root

COPY . /home/app
WORKDIR /home/app
RUN python -m venv .venv
RUN source /home/app/.venv/bin/activate
RUN pip install -r /home/app/requirements.txt
# RUN python test3.py