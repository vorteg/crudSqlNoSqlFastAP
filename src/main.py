import uvicorn
from config.app_config import app
from routes import users_route as users


from data.graphql_schemas.schemas import schema
from starlette.graphql import GraphQLApp


app.include_router(users.router)


@app.get("/", tags=["main"])
async def read_root():
    return {"Hello": "World"}

app.add_route("/graphql/", GraphQLApp(schema=schema))

#"ho"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
