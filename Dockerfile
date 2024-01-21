FROM python:3.12
COPY . .
WORKDIR .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "simple_API:app", "--host", "0.0.0.0"]