# Using the app

There are two ways to use this application

## Docker

### Linux distros

- Please follow steps to install docker engine for you operating system [here](https://docs.docker.com/engine/install/)
- Once you have docker engine installed on your system download and extract [release v1.0.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.0.0/v1.0.0.zip)
- Run the startApp shell script 
   ```bash
   ./startApp.sh
   ```
   - If the script does not run try again after making the script executable using 
      ```bash
      chmod +x startApp.sh
      ```
- Visit [localhost:8080/](localhost:8080/) to start using the app.

### Mac OS

- Please follow steps to install docker desktop for you operating system [here](https://www.docker.com/get-started/)
- Once you have docker desktop installed on your system download and extract [release v1.0.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.0.0/v1.0.0.zip)
- Run the startApp shell script 
   ```bash
   ./startApp.sh
   ```
   - If the script does not run try again after making the script executable using 
      ```bash
      chmod +x startApp.sh
      ```
- Visit [localhost:8080/](localhost:8080/) to start using the app.

### Windows

- Please follow steps to install docker desktop for you operating system [here](https://www.docker.com/get-started/)
- Once you have docker desktop installed on your system download and extract [release v1.0.0](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/releases/download/v1.0.0/v1.0.0.zip)
- Run the startApp shell script 
   ```bash
   ./startApp.sh
   ```
   - If the script does not run try again after making the script executable using 
      ```bash
      chmod +x startApp.sh
      ```
- Visit [localhost:8080/](localhost:8080/) to start using the app.

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

- Backend runs on the port defined in backend env file (e.g., localhost:3333).

# Experiment Replication

To replicate the experiment and to see the results, switch to the ```experiment``` branch and follow the instructions in the README.md file by clicking [here](https://github.com/aakarshanbasubhardwaj/timeSeriesDataSynchronisation/tree/experiment)