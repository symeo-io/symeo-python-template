from pydantic.main import BaseModel


class UserDTO(BaseModel):
    user_id: str
    username: str
