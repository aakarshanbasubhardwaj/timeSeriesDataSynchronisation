## Local Development

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
