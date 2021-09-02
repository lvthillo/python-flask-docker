FROM public.ecr.aws/sam/build-python3.6:latest
LABEL maintainer="lorenz.vanthillo@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install codeguru_profiler_agent
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
