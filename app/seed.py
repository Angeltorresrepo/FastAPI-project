# seed.py

from sqlalchemy.orm import Session
from .models import User, Post, Vote
from .utils import hash  # suponiendo que tienes un hasher

def seed_data(db: Session):
    # Borra todo primero si quieres limpiar la tabla
    db.query(Post).delete()
    db.query(User).delete()
    db.query(Vote).delete()

    # Crear usuarios
    user1 = User(email="test1@example.com", password=hash("1234"))
    user2 = User(email="test2@example.com", password=hash("1234"))
    user3 = User(email="test3@example.com", password=hash("1234"))
    user4 = User(email="test4@example.com", password=hash("1234"))
    user5 = User(email="test5@example.com", password=hash("1234"))
    user6 = User(email="test6@example.com", password=hash("1234"))
    user7 = User(email="test7@example.com", password=hash("1234"))


    db.add_all([user1, user2, user3, user4, user5, user6, user7])
    db.commit()

    # Crear posts asociados
    post1 = Post(title="Primer post", content="Contenido de prueba", owner_id=user1.id)
    post2 = Post(title="Segundo post", content="Otro contenido", owner_id=user2.id)
    post3 = Post(title="Tercer post", content="Más contenido", owner_id=user1.id)
    post4 = Post(title="Cuarto post", content="Contenido adicional", owner_id=user2.id)
    post5 = Post(title="Quinto post", content="Contenido extra", owner_id=user3.id)
    post6 = Post(title="Sexto post", content="Contenido extra", owner_id=user4.id)
    post7 = Post(title="Séptimo post", content="Contenido extra", owner_id=user5.id)
    post8 = Post(title="Octavo post", content="Contenido extra", owner_id=user6.id)
    post9 = Post(title="Noveno post", content="Contenido extra", owner_id=user7.id)
    post10 = Post(title="Décimo post", content="Contenido extra", owner_id=user1.id)
    post11 = Post(title="Undécimo post", content="Contenido extra", owner_id=user7.id)
    post12 = Post(title="Duodécimo post", content="Contenido extra", owner_id=user3.id)
    post13 = Post(title="Decimotercer post", content="Contenido extra", owner_id=user4.id)
    post14 = Post(title="Decimocuarto post", content="Contenido extra", owner_id=user5.id)
    post15 = Post(title="Decimoquinto post", content="Contenido extra", owner_id=user6.id)
    post16 = Post(title="Decimosexto post", content="Contenido extra", owner_id=user7.id)
    post17 = Post(title="Decimoséptimo post", content="Contenido extra", owner_id=user6.id)
    post18 = Post(title="Decimoctavo post", content="Contenido extra", owner_id=user2.id)
    post19 = Post(title="Decimonoveno post", content="Contenido extra", owner_id=user3.id)
    post20 = Post(title="Vigésimo post", content="Contenido extra", owner_id=user4.id)
    post21 = Post(title="Vigésimo primer post", content="Contenido extra", owner_id=user5.id)

    db.add_all([post1, post2, post3, post4, post5, post6, post7,
                post8, post9, post10, post11, post12, post13, post14,
                post15, post16, post17, post18, post19, post20, post21])
    db.commit()

    # Agregar likes:

    # Likes corregidos:

    # Agregar likes, sin duplicados y respetando que no vote su propio post

    like1 = Vote(user_id=user1.id, post_id=post9.id)  
    like2 = Vote(user_id=user1.id, post_id=post8.id)  
    like3 = Vote(user_id=user1.id, post_id=post15.id)
    like4 = Vote(user_id=user1.id, post_id=post2.id) 
    like5 = Vote(user_id=user1.id, post_id=post10.id)

    like6 = Vote(user_id=user2.id, post_id=post11.id) 
    like7 = Vote(user_id=user2.id, post_id=post9.id)  
    like8 = Vote(user_id=user2.id, post_id=post16.id)
    like9 = Vote(user_id=user2.id, post_id=post3.id) 
    like10 = Vote(user_id=user2.id, post_id=post4.id)

    like11 = Vote(user_id=user3.id, post_id=post14.id) 
    like12 = Vote(user_id=user3.id, post_id=post10.id)
    like13 = Vote(user_id=user3.id, post_id=post12.id)
    like14 = Vote(user_id=user3.id, post_id=post11.id)
    like15 = Vote(user_id=user3.id, post_id=post5.id) 

    like16 = Vote(user_id=user4.id, post_id=post7.id)  
    like17 = Vote(user_id=user4.id, post_id=post11.id)
    like18 = Vote(user_id=user4.id, post_id=post18.id)
    like19 = Vote(user_id=user4.id, post_id=post12.id)
    like20 = Vote(user_id=user4.id, post_id=post6.id) 

    like21 = Vote(user_id=user5.id, post_id=post8.id)  
    like22 = Vote(user_id=user5.id, post_id=post12.id)
    like23 = Vote(user_id=user5.id, post_id=post13.id)
    like24 = Vote(user_id=user5.id, post_id=post19.id)
    like25 = Vote(user_id=user5.id, post_id=post20.id)

    like26 = Vote(user_id=user6.id, post_id=post9.id)  
    like27 = Vote(user_id=user6.id, post_id=post13.id)
    like28 = Vote(user_id=user6.id, post_id=post14.id)
    like29 = Vote(user_id=user6.id, post_id=post20.id)
    like30 = Vote(user_id=user6.id, post_id=post17.id)

    like31 = Vote(user_id=user7.id, post_id=post1.id)  
    like32 = Vote(user_id=user7.id, post_id=post14.id)
    like33 = Vote(user_id=user7.id, post_id=post15.id)
    like34 = Vote(user_id=user7.id, post_id=post21.id)
    like35 = Vote(user_id=user7.id, post_id=post4.id)

    db.add_all([like1, like2, like3, like4, like5,
                like6, like7, like8, like9, like10,
                like11, like12, like13, like14, like15,
                like16, like17, like18, like19, like20,
                like21, like22, like23, like24, like25,
                like26, like27, like28, like29, like30,
                like31, like32, like33, like34, like35])
    db.commit()


