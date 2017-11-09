# -*- coding: utf-8 -*-
__author__ = 'huydq17'
from flask import Blueprint, jsonify, request, abort
from ..extensions import mongo, perms, resource, parser
from .. import exceptions
from marshmallow import fields
from sample_data import MINION_SAMPLE_DATA

api = Blueprint('api_minion', __name__, url_prefix='/api/v1/minion')


# Minion Status ********************************************************************************************************
# List minion
@api.route('/find', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'view_agent')
def list_minions():
    """
    List minions
    """
    params = {
        '_id': fields.String(),
        'comment': fields.String(),
        'connection_data': fields.String(),
        'os': fields.String(),
        'agent': fields.Boolean(),
        'cmdlog': fields.Boolean(),
        'connection': fields.Boolean(),
        'filebeat': fields.Boolean(),
        'kav': fields.Boolean(),
        'oa': fields.Boolean(),
        'ossec': fields.Boolean(),
        'group': fields.String(),
        'actor': fields.String(required=True),
        'count': fields.Integer(),
        'since': fields.Integer(),
        'sort': fields.Dict()
    }
    args = parser.parse(params)
    query = {}

    keys = ['filebeat', 'agent', 'connection', 'cmdlog', 'ossec', 'oa', 'kav']
    for k in keys:
        if k in args:
            v = args[k]
            if v:
                query[k] = args[k]
            else:
                query[k] = {'$ne': True}

    keys = ['_id', 'os', 'comment', 'connection_data']
    for k in keys:
        v = args.get(k, '').strip()
        if v and v != '*':
            query[k] = {'$regex': args[k].strip(), '$options': 'i'}

    group = args.get('group', '')
    if group:
        query['group'] = group

    sort_key = '_id'
    sort_value = 1
    if 'sort' in args:
        sort_key = args['sort']['key']
        sort_value = int(args['sort']['value'])

    _sort = [(sort_key, sort_value)]

    data = mongo.db.minion.find(query).sort(_sort)
    count = data.count()

    if 'since' in args:
        data = data.skip(int(args['since']))
    if 'count' in args and args['count'] != -1:
        data = data.limit(int(args['count']))

    result = {'minions': list(data), 'count': count}

    # Sample data if there is not DB
    # result = MINION_SAMPLE_DATA
    return jsonify(result)


# View an minion
@api.route('/view', methods=['GET'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'view_agent')
def view_minion():
    """
    Xem chi tiêt một minion
    """
    params = {
        '_id': fields.String(),
        'actor': fields.String(required=True)
    }
    args = parser.parse(params)

    query = {
        '_id': args['_id']
    }

    data = mongo.db.minion.find_one(query)
    if not data:
        raise exceptions.BadRequest(1006)

    return jsonify({'minion': data})


# Add new minion
@api.route('/add', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def add_minion():
    """
    Thêm một minion mới
    """
    params = {
        '_id': fields.String(required=True),
        'comment': fields.String(),
        'filebeat': fields.Boolean(required=True),
        'agent': fields.Boolean(required=True),
        'connection': fields.Boolean(required=True),
        'cmdlog': fields.Boolean(required=True),
        'os': fields.String(),
        'ossec': fields.Boolean(required=True),
        'connection_data': fields.String(),
        'oa': fields.Boolean(required=True),
        'kav': fields.Boolean(required=True),
        'group': fields.String(),
        'actor': fields.String(required=True)
    }
    json_data = parser.parse(params)
    _id = json_data['_id'].strip()

    data = [row for row in mongo.db.minion.find({'_id': _id})]
    if len(data) > 0:
        raise exceptions.BadRequest(1005, '_id')

    new_minion = {
        '_id': _id,
        'filebeat': json_data['filebeat'],
        'agent': json_data['agent'],
        'connection': json_data['connection'],
        'cmdlog': json_data['cmdlog'],
        'os': json_data.get('os', ''),
        'ossec': json_data['ossec'],
        'connection_data': json_data.get('connection_data', ''),
        'oa': json_data['oa'],
        'kav': json_data['kav'],
        'comment': json_data.get('comment', '')
    }

    mongo.db.minion.insert(new_minion)
    return jsonify({'_id': _id})


# Edit an minion
@api.route('/edit', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def edit_minion():
    """
    Update an minion
    """
    params = {
        '_id': fields.String(required=True),
        'comment': fields.String(),
        'filebeat': fields.Boolean(allow_none=True),
        'agent': fields.Boolean(allow_none=True),
        'connection': fields.Boolean(allow_none=True),
        'cmdlog': fields.Boolean(allow_none=True),
        'os': fields.String(),
        'ossec': fields.Boolean(allow_none=True),
        'connection_data': fields.String(),
        'oa': fields.Boolean(allow_none=True),
        'kav': fields.Boolean(allow_none=True),
        'actor': fields.String(required=True)
    }
    json_data = parser.parse(params)

    query_params = {
        '_id': json_data['_id']
    }

    data = mongo.db.minion.find_one(query_params)
    if not data:
        raise exceptions.BadRequest(1006)

    update_data = {}
    keys = ['comment', 'filebeat', 'agent', 'connection', 'cmdlog', 'os', 'ossec', 'connection_data', 'oa', 'kav']
    for k in keys:
        if k in json_data:
            update_data[k] = json_data[k]

    mongo.db.minion.update(query_params, {'$set': update_data})
    return jsonify({'minion': query_params})


# Delete an minion
@api.route('/delete', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def delete_minion():
    """
    Delete an minion
    """
    params = {
        '_id': fields.String(required=True)
    }

    json_data = parser.parse(params)
    query_params = {
        '_id': json_data['_id']
    }

    data = mongo.db.minion.find_one(query_params)
    if not data:
        raise exceptions.BadRequest(1006)

    mongo.db.minion.remove(query_params)
    return jsonify({'minion': query_params})