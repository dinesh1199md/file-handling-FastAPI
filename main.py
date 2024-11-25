from fastapi import FastAPI,status,File,UploadFile,HTTPException
from typing import List
import os,shutil,json
from fastapi.responses import FileResponse
import yaml

app=FastAPI()

# Upload single file
@app.post("/uploadfile1/")
async def upload_file(file: UploadFile ):
    os.makedirs("uploads", exist_ok=True)  # Ensure the uploads directory exists
    with open(f"uploads/{file.filename}", "w") as buffer:
        shutil.copyfileobj(file.file, buffer)
        pass
    return {"filename": file.filename}

# Upload multiple files
@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile]):
    os.makedirs("uploads", exist_ok=True)  # Ensure the uploads directory exists
    filenames = []
    for file in files:
        with open(f"uploads/{file.filename}", "w") as buffer:
            shutil.copyfileobj(file.file, buffer)
        filenames.append(file.filename)
    return {"filenames": filenames}

# Download a file
@app.get("/downloadfile/{filename}")
async def download_file(filename: str):
    file_path = f"uploads/{filename}"
    
    # Check if the file exists
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "File not found"}
    
