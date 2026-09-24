from pydantic import BaseModel, EmailStr


# Create User class witht the help of BaseModel for Validation
class User(BaseModel):
    id: int  # Select the data type of class member
    name: str
    sign_ts: str | None = None
    isActive: bool
    email: EmailStr


# Create the Object using User Class
objUser = User(id=123, name="Gop", isActive=False, email="gop2026@gmail.com")
print(objUser)
