# Recursive / Self-Reference Nested Models

from pydantic import BaseModel
from typing import Optional,List

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List['Comment']] = None

Comment.model_rebuild()

comment_1 = Comment(
    id = 1, content= "hello sir",
    replies=[
        Comment(id=2, content="hello mam"),
        Comment(id=3, content="Good afternoon",
                replies=[
                    Comment(id=4, content="more reply comment")
                ])
    ]
)

print(comment_1.replies[0].id)
print(comment_1.replies[1].replies[0].content)



