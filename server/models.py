# Add models for Users, music Links, Friends , Lists, Music In lists, Favorites
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, bcrypt
from flask import abort

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User( db.Model ):
    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key=True )
    username = db.Column( db.String )
    email = db.Column( db.String, unique = True )
    password = db.Column( db.Text )
    image = db.Column( db.String, default="https://vdostavka.ru/wp-content/uploads/2019/05/no-avatar.png" )
    lists = db.relationship( "List", backref = "user" )

    def authenticate( self, password ):
        return bcrypt.check_password_hash(
            self.password, password.encode( 'utf-8' )
        )

class List( db.Model ):
    __tablename__ = 'songs'

    id = db.Column( db.Integer, primary_key=True )
    title = db.Column( db.String )
    cover = db.Column( db.String )
    singer = db.Column( db.String )

class List( db.Model ):
    __tablename__ = 'lists'

    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String )
    user_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    songs = db.relationship( "SongsInList", backref = "list")

class SongsInList( db.Model ):
    __tablename__ = 'songs-in-lists'

    id = db.Column( db.Integer, primary_key=True )
    song_name = db.Column( db.String )
    song_cover = db.Column( db.String )
    song_id = db.Column( db.Integer, db.ForeignKey( 'songs.id' ) )
    list_id = db.Column( db.Integer, db.ForeignKey( 'lists.id' ) )
    user_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
