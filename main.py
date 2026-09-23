from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Make List with Dictionary
courses_list = [
    {
        "id": 1,
        "course": "MCA",
        "semester": 4,
        "subjects": "Python, FastAPI, Research Methodology, Linux",
    },
    {
        "id": 2,
        "course": "BscIT-Hons",
        "semester": 8,
        "subjects": "C, C++, Java, Networking, Database",
    },
    {
        "id": 3,
        "course": "BscIT-CS",
        "semester": 6,
        "subjects": "Linux, Server, Virtual Machine, Python",
    },
    {
        "id": 4,
        "course": "MscIT(AI&ML)",
        "semester": 4,
        "subjects": "Python, Research Methodology, Matplotlib,SPSS, R Programming",
    },
]

# add path of Templates
templates = Jinja2Templates(directory="./templates")


@app.get("/")  # Vist Home Page
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"courses": courses_list})


# File Uploading - Load the View
@app.get("/upload")
def upload_file(request: Request):
    return templates.TemplateResponse(request, "upload.html")


# File Uploading - Process of file uploading....
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"message": "File Uploaded succesfully...."}


# @app.get("/contactus")  # Visit Contact Us Page
# def contactus():,
#     return {"contact": "www.ganpatuniversity.ac.in"}
