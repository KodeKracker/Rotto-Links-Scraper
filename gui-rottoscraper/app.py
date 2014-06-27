#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import settings
from flask import Flask
from flask import request
from flask import session
from flask import g
from flask import redirect
from flask import url_for
from flask import abort
from flask import render_template
from flask import flash
from flask.views import MethodView

class RottoView(MethodView):
    def get(self):
        return render_template('main.html')


app = Flask(__name__)
app.config.from_object(settings)


app.add_url_rule('/', view_func=RottoView.as_view('rotto_view'),
    methods=['GET',])


if __name__ == '__main__':
    app.run()