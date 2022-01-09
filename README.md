## _Application using Django 3.2.7_

### Options for running the application
1. **Using Virtual Environment**
if you want to run this application using virtual environment make sure you've **python3** and **pip** installed on your operating system
    ```console
        python -m venv venv
    ```
    or
    ```console
        python3 -m venv venv
    ```
    or
    ```console
        py -m venv venv
    ```
    
    Then activate virtual environment and install packages
    ```console
        venv\Script\activate
        pip install -r requirements.txt
    ```
    
    To run application 
    ```console
        python manage.py runserver
    ```
    
    To create user for login to application
    ```console
        python manage.py createsuperuser
    ```
2. **Using Docker Composer**
if you want to run this application using docker, make sure you've installed docker and docker compose (well tested in Docker version **20.10.11** & docker-compose version **1.21.2**)

    ```console
    docker-compose -f docker-compose.dev.yaml up -d
    ```
