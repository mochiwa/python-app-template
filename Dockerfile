FROM python:3.10.12-bullseye

COPY src ./src
COPY script ./script
COPY pyproject.toml ./

RUN pip install -e .

CMD ["python", "./script/main.py"]