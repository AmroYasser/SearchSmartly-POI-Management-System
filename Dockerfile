FROM python

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    libgdal-dev \
    gdal-bin \
    binutils \
    libproj-dev

RUN pip install GDAL==$(gdal-config --version)

ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

COPY . .
