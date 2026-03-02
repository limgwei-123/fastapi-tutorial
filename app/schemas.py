from pydantic import BaseModel

class PostCreate(BaseModel):
  title: str
  content: str

class PostResponses(BaseModel):
  title: str
  content: str