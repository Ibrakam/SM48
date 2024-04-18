import sqlalchemy

from database.models import User
from datetime import datetime
from database import get_db
from database.security import create_access_token


# регистрация юзера
def register_user_db(username, email, password, phone_number, user_city):
    db = next(get_db())
    new_user = User(username=username, email=email, password=password, phone_number=phone_number,
                    user_city=user_city, reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return new_user.idd


# проверка на наличие юзера в бд
def check_user_db(phone_number, email):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number,
                                       email=email).first()
    if checker:
        return False
    return True


# вход в аккаунт
def check_user_password_db(email, password):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()
    if checker:
        if checker.password == password:
            return checker.id
        else:
            return "Неверный пароль"
    else:
        return 'Неверная почта'


# все данные о пользователе
def profile_info_db(user_id):
    db = next(get_db())
    all_info = db.query(User).filter_by(id=user_id).first()
    if all_info:
        return (all_info.email, all_info.phone_number,
                all_info.username, all_info.user_city, all_info.reg_date)
    return 'Пользователь не найден'


# изменение данных
def change_user_data(user_id, changeable_info, new_data):
    db = next(get_db())
    all_info = db.query(User).filter_by(id=user_id).first()
    if all_info:
        if changeable_info == "email":
            all_info.email = new_data
        elif changeable_info == "phone_number":
            all_info.phone_number = new_data
        elif changeable_info == "user_city":
            all_info.user_city = new_data
        elif changeable_info == "password":
            all_info.password = new_data
        elif changeable_info == "name":
            all_info.name = new_data
        db.commit()
        return "Данные успешно изменены"
    return "Пользователь не найден"


def login_user_db(email, password):
    db = next(get_db())
    login = db.query(User).filter_by(email=email, password=password).first()
    if login:
        token_data = {"user_id": login.id}
        access_token_data = create_access_token(token_data)
        return {"access_token": access_token_data, "token_type": "Bearer", "status": "Success"}
    else:
        return 'Неверный мейл или пароль'