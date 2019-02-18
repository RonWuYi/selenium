FROM python:3.6

WORKDIR /selenium

COPY . /selenium

RUN pip install --trusted-host pypi.python.org -r requirement.txt

EXPOSE 80

ENV NAME World

CMD ["python", "upload_file_multiple.py"]