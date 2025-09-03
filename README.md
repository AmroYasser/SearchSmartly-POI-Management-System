# Django POI Management System

This is a Django-based Point of Interest (POI) management system that allows you to import POI data from various file formats (CSV, JSON, XML) and store it in a database. The system provides an admin interface to view and search for the POI data, including calculating the average rating for each POI. The project is set up to run using Docker.


## Features

- Import POI data from CSV, JSON, and XML files
- Store POI data in a database
- View and search for POI data through the Django admin interface
- Filter the POIs by category
- Calculate the average rating for each POI

## Prerequisites

- Python
- Django
- PostgreSQL
- Docker

## Installation

1. Clone the repository:
```bash
git clone link/to/the/repo
```

2. Make sure you are in the project root directory.

3. Build and start the Docker containers:
```bash
docker-compose up -d --build
```

4. Run the database migrations:
```bash
docker-compose run web python searchsmartly/manage.py makemigration

docker-compose run web python searchsmartly/manage.py migrate
```

5. Create a superuser account:
```bash
docker-compose run web python searchsmartly/manage.py createsuperuser
```

6. Access the application in your web browser at `http://localhost:8000/admin/`

## Usage

1. Prepare your POI data files in CSV, JSON, or XML format. The file formats should be as follows:
- CSV:
  ```csv
  poi_id, poi_name, poi_latitude, poi_longitude, poi_category, poi_ratings
  external_id,name,category,latitude,longitude,{rating1,rating2,...}
  ```
- JSON:
  ```json
  [
    {
      "id": "external_id",
      "name": "poi_name",
      "category": "poi_category",
      "coordinates": {
        "latitude": latitude_value,
        "longitude": longitude_value
      },
      "ratings": [rating1, rating2, ...]
    }
  ]
  ```
- XML:
  ```xml
  <DATA_RECORD>
    <pid>external_id</pid>
    <pname>poi_name</pname>
    <pcategory>poi_category</pcategory>
    <platitude>latitude_value</platitude>
    <plongitude>longitude_value</plongitude>
    <pratings>rating1,rating2,...</pratings>
  </DATA_RECORD>
  ```

2. Add the files into the project root directory.

3. Use the import command to import POI data from CSV, JSON, and/or XML files:
```bash
docker-compose run web python searchsmartly/manage.py import_poi_data pois.csv pois.json pois.xml
```

4. Log in to the Django admin interface using the superuser account you created during installation.

5. Go to the POI section in the admin interface.

6. View and search (using the internal/external id) for the imported POI data in the admin interface. The average rating for each POI will be calculated and displayed automatically. You can also filter by category.

