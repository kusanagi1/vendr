import sqlite3
from sqlite3.dbapi2 import PARSE_DECLTYPES

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    '''This returns a database connection'''
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    '''Closes a database connection if it exists'''
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """Initialize database when invoked"""
    db = get_db()

    with current_app.open_resource('schema.sql') as file:
        db.executescript(file.read().decode('utf-8'))

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command('init_db') 
@with_appcontext
def init_db_command():
    '''purge existing data and create new tables'''
    init_db()
    click.echo('Initialized the database.')

