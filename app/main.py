from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/detect_voice/")
async def detect_voice(file: UploadFile = File(...)):
    contents = await file.read()
    # Implement the voice detection logic here
    # For now, we will just return the file size as a placeholder
    return JSONResponse(content={'filename': file.filename, 'size': len(contents)})