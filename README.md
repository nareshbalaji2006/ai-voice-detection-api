# AI Voice Detection API

## Project Setup
To set up the AI Voice Detection API, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/nareshbalaji2006/ai-voice-detection-api.git
   ```
2. Navigate into the project directory:
   ```bash
   cd ai-voice-detection-api
   ```
3. Install the necessary dependencies:
   ```bash
   npm install
   ```

## Installation
Ensure you have Node.js and npm installed. You can download them from [Node.js official website](https://nodejs.org/).

### Running the Server
To start the server, run:
```bash
npm start
```

### API Documentation
- **Endpoint:** `/api/detect`
- **Method:** POST
- **Description:** Detects voice and processes input audio.
- **Request Body:** 
  ```json
  {
      "audio_file": "<base64_encoded_audio>"
  }
  ```
- **Responses:**
  - **200 OK:** Successfully detected voice.
  - **400 Bad Request:** Missing or invalid audio file.

For more details, refer to the [full API documentation](https://github.com/nareshbalaji2006/ai-voice-detection-api/wiki).
