# from typing import Union

# from database import DB

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/regsiter")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

from database import DB

if __name__ == "__main__":
  DB.set("")
  DB.prepare('select_theme')
  print(DB.get_prepared('select_theme'))