from fastapi import FastAPI
main  = FastAPI()
@main.get('/') #this the path/route
def index():
    return "This is the front page"
@main.get("/abaut")
def abaut():
    return "abaut page"


#creating dev blanche
@main.get("/dev")
def dev():
    return "development page"