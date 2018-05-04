FROM python:3.6

ARG project_dir=/app/

RUN pip install pipenv
RUN mkdir $project_dir

COPY ./Pipfile $project_dir
COPY ./Pipfile.lock $project_dir
COPY ./templates/ $project_dir/templates/
ADD ./app.py $project_dir
WORKDIR $project_dir

RUN pipenv install
# EXPOSE 5000
ENTRYPOINT ["pipenv", "run", "start"]

# CMD ["pipenv", "run", "start"]
# CMD ["python", "/app/app.py"]
