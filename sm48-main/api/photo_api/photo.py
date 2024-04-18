from fastapi import Request, Body, UploadFile, APIRouter
from database.photoservice import change_photo_db, delete_photo_db, get_all_or_exact_photo_db

photo_router = APIRouter(prefix='/photo', tags=['Управление фотографиями'])


# получение всех или одной фотки
@photo_router.get('/api/photos')
async def get_all_or_exact_photo(photo_id: int = 0, user_id: int = 0):
    if photo_id and user_id:
        exact_photo = get_all_or_exact_photo_db(photo_id, user_id)
        return {'status': 1, 'message': exact_photo}
    return {'status': 0, 'message': 'Ошибка'}


# изменить фото
@photo_router.put("/api/photo")
async def change_user_photo(photo_id: int = Body(...), photo_file: UploadFile = Body(...)):
    if photo_file:
        # сохранить фото в папку
        with open(f"{photo_id}.jpg", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
        change_photo_db(photo_id, f"/api/photo_api/photos/{photo_id}.jpg")
    return {"status": 1, "message": "Фото успешно изменено"}


# удалить фото
@photo_router.delete('/api/photos')
async def delete_user_photo(request: Request):
    data = await request.json()
    photo_id = data.get('photo_id')
    if photo_id:
        delete_photo_db(photo_id)
        return {'status': 1, 'message': 'Фото успешно удалено'}
    return {'status': 0, 'message': 'Ошибка'}
