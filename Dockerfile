FROM python:3.10.12-bullseye

COPY src ./src
COPY script ./script
COPY pyproject.toml requirements.txt setup.cfg setup.py ./

RUN pip install -e .

CMD ["python", "./script/main.py"]