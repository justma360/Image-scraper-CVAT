# CVAT Local Labeling

## Requirements

1. Python 3.8 (with venv)
2. Docker
3. NodeJS

## Installation

### Python

1. Install Python 3.8 onto computer

```cmd
  python -m venv venv
```

```cmd
  pip install -r requirements.txt
```

### CVAT

1. Download and install [Docker](https://www.docker.com/)
2. Install Window Linux Subsystem by following these [Instructions](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
3. Build the docker compose with the command below

```cmd
  docker-compose up -d
```

4. CVAT (labeling) Service will be hosted on

```
  http://localhost:8080/
```

## Usage

### Python Scripts

```
similarity.py
```

1. Changes format of all downloaded images to .jpg
2. Checks for duplicate images
3. Resets index for all the missing files

### CVAT Server
**Note** If starting on a new computer all previous data will be lost (unless you migrate the docker containers) as the data is stored in the DOCKER containers.

1. Start CVAT server and connect to `http://localhost:8080/`
2. Create an account (Enter random details unless hosted on server)
3. Create new project (+) (According to the object or the project for labeling ). Fill in the field
   - Name: Objects to detect (Hoverboards - with "s")
   - Constructor -> Add Label -> Label Name: Object to detect (Hoverboard without "s")
   - `Create and open` the project
     ![create_project](md\images\create_project.png)
4. Create new task (+)
   - Name: Label object to be labelled
   - Select files: select files from google downloaded `photos/<object>`
   - Config the Advance Config as below

     ![create_task](md\images\create_task.png)

     ![create_task_config](md\images\create_task_config.png)
5. Click on `Job #<number>` to enter the job and start labeling
6. Labeling keyshortcuts
   - D: Previous
   - F: Next
   - N: New box (2 points)
7. Press Save -> Export Job Data Set -> Export as Yolo Format


# Notes
1. The server is hosted on Docker container, the information regarding the server is stored in the container.
2. Data should be exported when finished.
