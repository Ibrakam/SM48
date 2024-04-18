from fastapi import Request, APIRouter
from database.postservice import get_all_or_exact_post_db, change_post_text_db, delete_exact_post_db

posts_router = APIRouter(prefix='/post', tags=['Управление постами'])


# получить определенный или все посты
@posts_router.get('/api/posts')
async def get_all_or_exact_post(post_id: int = 0):
    if post_id:
        exact_post = get_all_or_exact_post_db(post_id)
        return {"status": 1, "message": exact_post}
    return {"status": 0, "message": "Ошибка"}


# изменить пост
@posts_router.put('/api/posts')
async def change_user_post(requests: Request):
    data = requests.json()
    post_id = data.get('post_id')
    text = data.get('text')
    if post_id and text:
        change_post_text_db(post_id=post_id, text=text)
        return {"status": 1, "message": "Успешно изменено"}
    return {"status": 0, "message": "Ошибка"}


# удалить пост
@posts_router.delete('/api/posts')
async def delete_user_post(request: Request):
    data = await request.json()
    post_id = data.get('post_id')
    if post_id:
        delete_exact_post_db(post_id)
        return {"status": 1, "message": "Фото успешно удалено"}
    return {"status": 0, "message": "Ошибка"}
