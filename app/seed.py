# seed.py

from sqlalchemy.orm import Session
from .models import User, Post
from .utils import hash  # suponiendo que tienes un hasher

def seed_data(db: Session):
    # Borra todo primero si quieres limpiar la tabla
    db.query(Post).delete()
    db.query(User).delete()

    # Crear usuarios
    user1 = User(email="test1@example.com", password=hash("1234"))
    user2 = User(email="test2@example.com", password=hash("1234"))

    db.add_all([user1, user2])
    db.commit()

    # Crear posts asociados
    post1 = Post(title="Primer post", content="Contenido de prueba", owner_id=user1.id)
    post2 = Post(title="Segundo post", content="Otro contenido", owner_id=user2.id)

    db.add_all([post1, post2])
    db.commit()
