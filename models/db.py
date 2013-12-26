db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
auth = Auth(db)
auth.define_tables()
crud = Crud(db)

db.define_table('post',
    Field('title'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(title)s')


db.define_table('document',
    Field('post_id', 'reference post'),
    Field('name'),
    Field('file', 'upload'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(name)s')


db.define_table('comment',
    Field('post_id', 'reference post'),
    Field('comment', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(name)s')

db.post.title.requires = IS_NOT_IN_DB(db, 'post.title')
db.post.body.requires = IS_NOT_EMPTY()
db.post.created_by.readable = db.post.created_by.writable = False
db.post.created_on.readable = db.post.created_on.writable = False

db.comment.comment.requires = IS_NOT_EMPTY()
db.comment.created_by.readable = db.comment.created_by.writable = False
db.comment.created_on.readable = db.comment.created_on.writable = False

db.document.name.requires = IS_NOT_IN_DB(db, 'document.name')
db.document.post_id.readable = db.document.post_id.writable = False
db.document.created_by.readable = db.document.created_by.writable = False
db.document.created_on.readable = db.document.created_on.writable = False