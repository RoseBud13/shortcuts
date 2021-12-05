"""
commands.py
- provides a command line utility for interacting with the
  application to perform interactive debugging and setup

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

import click

from flask import Blueprint
from appapi.models import db, Card

cmd = Blueprint('cmd', __name__)

@cmd.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@cmd.cli.command()
def forgecards():
    """Generate cards data."""
    db.create_all()

    cards = [
        {'cardType': 'main', 'cardBgColor': '#7089AC', 'cardBgOpacity': 1, 'cardHeight': '200px'},
        {'cardType': 'main', 'cardBgColor': '#C8C9C7', 'cardBgOpacity': 1, 'cardHeight': '150px'},
        # {'cardType': 'cluster', 'cardBgColor': '#141414', 'cardBgOpacity': 1, 'cardHeight': '160px'},
        # {'cardType': 'main', 'cardBgColor': '#D9B48B', 'cardBgOpacity': 1, 'cardHeight': '170px'},
        # {'cardType': 'main', 'cardBgColor': '#DDA69D', 'cardBgOpacity': 1, 'cardHeight': '300px'},
        # {'cardType': 'cluster', 'cardBgColor': '#A3B2A4', 'cardBgOpacity': 1, 'cardHeight': '160px'},
    ]

    for c in cards:
        card = Card(cardType=c['cardType'], cardBgColor=c['cardBgColor'], cardBgOpacity=c['cardBgOpacity'], cardHeight=c['cardHeight'])
        db.session.add(card)

    db.session.commit()
    click.echo('Cards Done.')
