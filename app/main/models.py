#!/usr/bin/env python
# coding: utf-8

from .. import db


class GitProject(db.Model):
    __tablename__ = 'gitproject'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    addr = db.Column(db.String(80), unique=True)
    des = db.Column(db.String(160), default=False)

    def __repr__(self):
        return '<GitProject %r>' % self.name

