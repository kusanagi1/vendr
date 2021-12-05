from logging import error
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from blog import db

from blog.auth import login_required
from blog.db import get_db

bp = Blueprint('blog', __name__)

def get_itemorder(id, check_author=True):
    order = get_db().execute(
        'SELECT p.id, item, item_description, quantity, created, author_id, username'
        ' FROM itemorder p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()
    
    if order is None:
        abort(404, "Item order id {0} doesn't exist".format(id))
      
    if check_author and order['author_id'] != g.user['id']:
        abort(403)
        
    return order  

@bp.route('/')
def index():
    db = get_db()
    orders = db.execute(
        'SELECT p.id, item, item_description, quantity, created, author_id, username'
        ' FROM itemorder p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    
    return render_template('blog/index.html', orders=orders)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        item = request.form['item']
        item_description = request.form['item_description']
        quantity = request.form['quantity']
        error = None
        
        if not item:
            error = 'item is required'
            
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO itemorder (item, item_description, quantity, author_id)'
                ' VALUES (?, ?, ?, ?)',
                (item, item_description, quantity, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    order = get_itemorder(id)
    
    if request.method == 'POST':
        item = request.form['item']
        item_description = request.form['item_description']
        quantity = request.form['quantity']
        error = None
        
        if not item:
            error = 'Item is required.'
            
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE itemorder SET item = ?, item_description = ?, quantity = ?'
                ' WHERE id = ?',
                (item, item_description, quantity, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))
        
    return render_template('blog/update.html', order=order)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_itemorder(id)
    db = get_db()
    db.execute('DELETE FROM itemorder WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))