from database.models import Comment, UserPost, Hashtag, PostPhoto
from database import get_db
from datetime import datetime


# получение всех или конкретного поста
def get_all_or_exact_post_db(post_id):
    db = next(get_db())
    if post_id == 0:
        return db.query(UserPost).all()
    return db.query(UserPost).filter_by(id=post_id).first()


# редактирование поста
def change_post_text_db(post_id, new_text):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    if exact_post:
        exact_post.main_text = new_text
        db.commit()
        return "Успешно изменено"
    return "Ошибка"


# удаление постаv
def delete_exact_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    if exact_post:
        db.delete(exact_post)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"


def public_comment_db(user_id, post_id, text):
    db = next(get_db())
    new_comment = Comment(post_id=post_id,
                          user_id=user_id, text=text, reg_date=datetime.now())
    db.add(new_comment)
    db.commit()
    return "Комментарий опубликован"


def get_exact_post_comment_db(post_id):
    db = next(get_db())
    exact_post_comments = db.query(Comment).filter_by(post_id=post_id).all()
    if exact_post_comments:
        return exact_post_comments
    return []


def change_comment_text_db(comment_id, new_text):
    db = next(get_db())
    exact_post = db.query(Comment).filter_by(id=comment_id).first()
    if exact_post:
        exact_post.text = new_text
        db.commit()
        return "Текст успешно изменен"
    return "Ошибка"


def delete_exact_comment_db(comment_id):
    db = next(get_db())
    exact_post = db.query(Comment).filter_by(id=comment_id).first()
    if exact_post:
        db.delete(exact_post)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"


# хештэги
def get_some_hashtags_db(size):
    db = next(get_db())
    some_hashtags = db.query(Hashtag).all()
    return some_hashtags[:size]


def get_exact_hashtag_db(hashtag_name):
    db = next(get_db())
    exact_hashtag = db.query(Hashtag).filter_by(hashtag_name=hashtag_name).first()
    if exact_hashtag:
        return exact_hashtag
    return []
