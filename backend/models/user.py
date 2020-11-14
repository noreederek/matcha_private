import hashlib
import uuid

from datetime import datetime

from pymysql.err import IntegrityError
from models import Model, Field, Subquery
from models.images import Image

from database import pool

class User(Model):
    table_name = "users"

    id = Field(int, modifiable=False)
    fname = Field(str)
    lname = Field(str)
    email = Field(str)
    username = Field(str)
    passhash = Field(str, hidden=True)
    email_verified = Field(bool, default=False)
    bio = Field(str)
    gender = Field(str)
    dob = Field(datetime)
    longitude = Field(float)
    latitude = Field(float)
    heat = Field(Subquery, Subquery("""
        (SELECT 
            IF(COUNT(id) = 0, 3, SUM(rating)) / IF(COUNT(id) = 0, 1, COUNT(id))
         FROM matches WHERE matchee_id = users.id and rating > 0) 
         AS heat
         """
        ))
    online = Field(bool)
    date_lastseen = Field(datetime)
    interests = Field(list)
    preferences = Field(list)
    deleted = Field(bool, modifiable=False, hidden=True)
    is_admin = Field(bool)

    def before_init(self, data):
        if "password" in data:
            self.passhash.value = self.hash_password(data["password"])

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def get_messages(self, from_id):
        try:
            connection = pool.get_conn()

            with connection.cursor() as c:
                c.execute("""SELECT * FROM messages 
                        WHERE 
                            (to_id=%s OR from_id=%s) 
                                AND 
                            (to_id=%s OR from_id=%s)
                        ORDER BY id
                    
                    """, (self.id, self.id, from_id, from_id))
                return c.fetchall()

        except Exception as e:
            print("Could not get messages", str(e))
        finally:
            pool.release(connection)


    def check_password(self, password):
        _hash, salt = self.passhash.split(':')
        return _hash == hashlib.sha256(salt.encode() + password.encode()).hexdigest()

    def get_primary_image(self):
        if self.id:
            try:
                connection = pool.get_conn()
                with connection.cursor() as c:
                    c.execute("""SELECT image64, image_type FROM images WHERE user_id=%s ORDER BY id DESC LIMIT 1""", (self.id,))
                    result = c.fetchone()
                    image64 = None if not result else result["image64"]
                    image_type = None if not result else result["image_type"]
                    self.append_field("image64", Field(str, image64))
                    self.append_field("image_type", Field(str, image_type))
            except Exception as e:
                raise
            finally:
                pool.release(connection)


    def delete(self):

        if self.id:
            connection = self.pool.get_conn()
            with connection.cursor() as c:
                c.execute("""
                        UPDATE {0} SET deleted = 1
                         WHERE id='{1}'
                """.format(self.table_name, self.id))
                connection.commit()
            self.pool.release(connection)
        else:
            raise Exception("User not in database")

    def destroy(self):
        if self.id:
            connection = self.pool.get_conn()
            with connection.cursor() as c:
                c.execute("DELETE FROM users WHERE id=%s", self.id)
                connection.commit()
            self.pool.release(connection)
        else:
            raise Exception("User not in database")


def get_full_user(user_id):
    user = User.get(id=user_id)

    images = Image.get_many(user_id=user_id)

    # Get the images for that user
    user.append_field("images", Field(list, images))

    return user
