FROM python:3.12.7-slim-buster as base

FROM base as builder

ENV HOME_DIR=/home/app
WORKDIR $HOME_DIR

RUN python -m venv venv
ENV PATH="$HOME_DIR/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install --progress-bar off -r requirements.txt

FROM base

ENV HOME_DIR=/home/app

RUN groupadd -g 570 app && useradd --create-home -u 568 -g app app

COPY --from=builder /usr/local/lib/python3.7/  /usr/local/lib/python3.7/
COPY --from=builder $HOME_DIR/venv  $HOME_DIR/venv

ADD ./* $HOME_DIR/

ENV PATH="$HOME_DIR/venv/bin:$PATH"

USER app

WORKDIR $HOME_DIR

EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
