FROM python:3.13.5

WORKDIR /app/
COPY ./ip_data.xlsx ./
#copy 2 scripts (subnet_analyzer.py , visualize.py)
COPY ./*.py ./

USER root

#install dependencies for pandas & matplotlib
RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
   libpng-dev \
&& rm -rf /var/lib/apt/lists/*
RUN mkdir -p /app/output

#install python dependencies for our work
RUN pip install --no-cache-dir pandas matplotlib openpyxl

ENTRYPOINT ["python"]
CMD ["subnet_analyzer.py"]

