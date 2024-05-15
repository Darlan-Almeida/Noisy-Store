from app.models.user_model import User

def create_user(name, email, phone, role):
    user = User(name, email, phone, role)
    user.save()
    return user
