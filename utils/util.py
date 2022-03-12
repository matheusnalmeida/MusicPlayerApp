from flask import Request, session, g

def valid_acess(request: Request):
    if 'logged_user' not in session:
        if '/static/' in request.path:
            return True
        elif request.endpoint not in ('index', 'login', 'register'):
            return False         
    else:        
        g.logged_user = session['logged_user']

    return True