def index():
    #posts = db(db.post).selectAll()
    posts = db().select(db.post.id,db.post.title,orderby=db.post.title)
    return dict(posts=posts)

def newpost():
     form = SQLFORM(db.post).process(next=URL('index'))
     return dict(form=form)


def new():
     form = SQLFORM(db.post).process(next=URL('index'))
     return dict(form=form)

def my_form_processing(form):
    print 1

def newComment():
    post = db.post(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM.factory(Field('comment','text',requires=IS_NOT_EMPTY())).process()
    #form = SQLFORM(db.comment).process(next=URL('default/show',request.args(0)))
    #form.vars.post_id = request.args(0,cast=int)
    if form.accepted:
        #post_id = db.post.insert(name=form.vars.name,forum=forum.id)
        db.comment.insert(post_id=request.args(0,cast=int),comment=form.vars.comment)
        redirect(URL('default/show',request.args(0)))
    return locals()

def show():
    this_post = db.post(request.args(0,cast=int)) or redirect(URL('index'))
    comments = db(db.comment.post_id==request.args(0,cast=int)).select()
    count = db(db.comment.post_id==request.args(0,cast=int)).count()
    return dict(post=this_post,comments=comments,count=count)

@auth.requires_login()
def editpost():
    #form = db(db.post,session.args[0])
    this_post = db.post(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.post, this_post).process(next = URL('show',args=request.args))
    return dict(form=form)

def user():
     return dict(form=auth())
