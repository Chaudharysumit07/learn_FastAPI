from fastapi import FastAPI

# this instance name matters , as this is used to run the app using uvicorn
app= FastAPI()


@app.get("/")
#the function name does not matter, you can keep it same in other decorators but it is a good practice to keep it relevant
# also , this function name is used by FastAPI to generate the docs
def index():
    return {'data':{"name":"Hello , World!"}}

@app.get("/about") # this is a path operation decorator.
#"/about" is the path
# "get" is the HTTP method which is called operation
def about(): #this is path operation function
    return {'data':{'about':"This is a sample FastAPI application."}}


# FastAPI matches the routes in the order they are written. So, specific routes should be defined before dynamic routes to avoid conflicts.
@app.get("/blog/all")
def show_all_blogs():
    return {'data':{'blog_id':'all'}}


@app.get("/blog/{id}") #id is the path parameter and it is dynamic
# you can have multiple path parameters too like /blog/{id}/comment/{comment_id}
def show(id): #id is passed as an argument to the function. its type is STRING by default
    return {'data':{'blog_id':id}} 


@app.get("/blog/{id}/comments") #id is the path parameter and it is dynamic

def show(id : int): #id should be integer , so we are specifying the type here
    return {'comments':{'blog_id':id}}

