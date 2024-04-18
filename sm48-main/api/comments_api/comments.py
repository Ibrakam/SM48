from fastapi import Request, APIRouter
from database.postservice import (get_exact_post_comment_db, public_comment_db,
                                  change_comment_text_db, delete_exact_comment_db)

comment_router = APIRouter(prefix='/comment', tags=['Управление комментами'])


@comment_router.post("/api/comment")
async def public_comment(request: Request):
    data = await request.json()
    post_id = data.get("post_id")
    user_id = data.get("user_id")
    text = data.get("main_text")
    if user_id and text and post_id:
        public_comment_db(user_id=user_id, post_id=post_id, text=text)
        return {"status": 1, "message": "Успешно опубликовано"}
    return {"status": 0, "message": "Ошибка"}


# получение комментов определенного постав
@comment_router.get("/api/comment")
async def get_exact_post_comments(request: Request):
    data = request.query_params
    post_id = data.get("post_id")
    if post_id:
        comments = get_exact_post_comment_db(post_id=post_id)
        return {"status": 1, "comments": comments}
    return {"status": 0, "message": "Ошибка"}


# изменить комментарий
@comment_router.put("/api/comment")
async def change_exact_user_comment(request: Request):
    data = await request.json()
    comment_id = data.get("comment_id")
    new_text = data.get("new_text")
    if comment_id and new_text:
        change_comment_text_db(comment_id=comment_id, new_text=new_text)
        return {"status": 1, "message": "Успешно изменено"}
    return {"status": 0, "message": "Ошибка"}


# удалить комментарий
@comment_router.delete("/api/comment")
async def delete_exact_user_comment(request: Request):
    data = request.query_params
    comment_id = data.get("comment_id")
    if comment_id:
        delete_exact_comment_db(comment_id=comment_id)
        return {"status": 1, "message": "Успешно удалено"}
    return {"status": 0, "message": "Ошибка"}


# удалить комментарий
@comment_router.delete("/api/comment")
async def delete_exact_user_comment(request: Request):
    pass
