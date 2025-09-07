# Contents
- [Using the tool](#using-the-tool)
- [Setup and Installation](#setup-and-installation)
- [Local Development](#local-development)
- [Experiment Replication](#experiment-replication)

# Using the tool

Once the tool is [set up and installed](#setup-and-installation) the following workflow can be used to synchronize two streams of 3d accelerometer data.

1. Access the frontend at [localhost:8080/](localhost:8080/) when running via Docker, or at or [localhost:8051/](localhost:8051/) when using the Python GUI.

2. Drag and drop or click to upload files to be synchronized.
   - Only csv files can be uploaded for synchronization.
   - The files each must have 3 columns with the first, second and third column corresponding to the x, y and z axis readings of the accelerometer respectively.
   - The total file size of the files must not exceed 50 MB.
3. A graph showing the plots of the uploaded files will be rendered below.
4. Click the Sync button to synchronize the files.
   - The synchronized files are visualized in the frontend.
5. Upon completion the files will be available for download as a zip.

# Setup and Installation

There are two ways to use this tool, follow the steps based on your desired way and operating system.

- [Python GUI](#a-python-gui)
   - [Linux](#linux)
   - [Mac OS](#mac-os)
   - [Windows](#windows)
- [Docker](#b-docker)
   - [Linux](#linux-1)
   - [Mac OS](#mac-os-1)
   - [Windows](#windows-1)

## A. Python GUI

### Linux

1. Make sure Python is installed on your system. 

2. After installing Python, download and extract [release v1.1.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.1.0/v1.1.0.tar.gz) - v1.1.0.tar.gz

3. Navigate to *PythonGUI* directory in the extracted release folder
```bash
cd PythonGUI
```

4. Run the startApp shell script from terminal using
```bash
./startApp.sh
```

   - If the script does not run try again after making the script executable using 
      ```bash
      chmod +x startApp.sh
      ```

5. Visit [localhost:8501/](localhost:8501/) to start using the tool.

### Mac OS

1. Make sure Python is installed on your system. 

2. After installing Python, download and extract [release v1.1.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.1.0/v1.1.0.tar.gz) - v1.1.0.tar.gz

3. Navigate to *PythonGUI* directory in the extracted release folder
```bash
cd PythonGUI
```

4. Run the startApp shell script from terminal using
```bash
./startApp.sh
```

   - If the script does not run try again after making the script executable using 
      ```bash
      chmod +x startApp.sh
      ```

5. Visit [localhost:8501/](localhost:8501/) to start using the tool.

### Windows

1. Make sure Python and GCC (C compiler) are installed on your system. 

2. After installing both, download and extract [release v1.1.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.1.0/v1.1.0.tar.gz) - v1.1.0.tar.gz

3. You can start the tool by navigating to *PythonGUI* folder in the extracted release folder

4. Double-click the *startApp.bat* file in the extracted folder (no command prompt needed).

5. Visit [localhost:8501/](localhost:8501/) to start using the tool.

## B. Docker

### Linux

1. Please follow steps to install docker engine for you operating system [here](https://docs.docker.com/engine/install/) and [Post Install Instructions here](https://docker-docs.uclv.cu/engine/install/linux-postinstall/)

   - If the post install instructions are not followed, the shell script must be executed using *sudo*.

2. Once you have docker engine installed on your system download and extract [release v1.1.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.1.0/v1.1.0.tar.gz)

3. Navigate to *Docker* directory in the extracted release folder
```bash
cd Docker
```

4. Run the *startApp* shell script from terminal using
```bash
./startApp.sh
```

   - If the script does not run try again after making the script executable using 
      ```bash
      chmod +x startApp.sh
      ```

5. Visit [localhost:8080/](localhost:8080/) to start using the tool.

### Mac OS

1. Please follow steps to install docker desktop for you operating system [here](https://www.docker.com/get-started/)

2. Once you have docker desktop installed on your system download and extract [release v1.1.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.1.0/v1.1.0.tar.gz)

3. Navigate to *Docker* directory in the extracted release folder
```bash
cd Docker
```

4. Run the startApp shell script from terminal using
```bash
./startApp.sh
```

   - If the script does not run try again after making the script executable using 
      ```bash
      chmod +x startApp.sh
      ```

5. Visit [localhost:8080/](localhost:8080/) to start using the tool.

### Windows

1. Please follow steps to install docker desktop for your operating system [here](https://www.docker.com/get-started/)

2. Once you have docker desktop installed on your system, download and extract [release v1.1.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.1.0/v1.1.0.tar.gz)

3. You can start the tool by navigating to *Docker* folder in the extracted release folder

4. Double click the startApp.bat file 

5. Visit [localhost:8080/](localhost:8080/) to start using the tool.

# Local Development

1. **Clone the repository**
   ```bash
   git clone git@github.com:aakarshanbasubhardwaj/timeSeriesDataSynchronisation.git
   ```

2. **Open terminal and go to the backend folder in the repository :**
   
   ```bash
   cd timeSeriesDataSynchronisation/backend
   ```

3. **Install backend dependencies :**

   ```bash
   npm install
   ```

4. **Create a `.env` file in backend directory and add desired PORT :**

   ```
   PORT=3333
   ```
   - Note - The `API_BASE_URL` in `frontend/config.js` must point to the same port number as specified in `backend/.env` file. If choosing a different port in `backend/.env`, the same must be updated in `frontend/config.js`.

5. **Install python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

6. **Start backend server :**

   ```bash
   npm run server
   ```

7. **Open `frontend/index.html` in your browser to use the frontend**

- Note - Backend runs on the port defined in backend env file (e.g., localhost:3333).

# Experiment Replication

To replicate the experiment and to see the results, switch to the ```experiment``` branch and follow the instructions in the README.md file by clicking [here](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/tree/experiment)