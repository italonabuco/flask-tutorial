import sqlite3

import click
from flask import Flask, current_app, g


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db: sqlite3.Connection | None = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables"""
    init_db()
    print("Initialized the database.")


def init_app(app: Flask):
    # tells Flask to call that function when cleaning up after returning the response
    app.teardown_appcontext(close_db)
    #  adds a new command that can be called with the flask command
    app.cli.add_command(init_db_command)
