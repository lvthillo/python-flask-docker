# FROM python:3.13-alpine
# LABEL maintainer="bujjisreenivasulu@gmail.com"
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# ENV APP_PORT=8080
# EXPOSE 8080
# ENTRYPOINT ["python"]
# CMD ["src/app.py"]

FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ARG APP_PORT=7070
ENV APP_PORT ${APP_PORT}
EXPOSE 7070
ENTRYPOINT ["python"]
CMD ["src/app.py"]