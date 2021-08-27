from pydantic import BaseModel, Field

# You can see this `Field` addon on http://127.0.0.1:8000/docs --> Schemas
# or in redoc http://127.0.0.1:8000/redoc#operation/create_user__post
class User(BaseModel):
    name: str = Field(
        'Mustermann', 
        title='Username', 
        description='You can save the Username in this field'
    )
    email: str
    password: str

    # This will create an example entry in http://127.0.0.1:8000/redoc
    class Config:
        schema_extra = {
            "example": {
                "name": "Hans Wurst",
                "email": "hans.wurst@acme.ltd",
                "password": "secure1234",
            }
        }
