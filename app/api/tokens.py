#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import jsonify, g
from app import db
from app.api import bp
from .auth import basic_auth, token_auth


@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    # commit change in a higher level
    db.session.commit()
    return jsonify({'token': token})


@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    g.current_user.revoke_token()
    # commit change on a higher level
    db.session.commit()
    return '', 204
