# -*- coding: utf-8 -*-
__author__ = 'huydq17'
from flask import Blueprint, jsonify, request, abort
from ..extensions import mongo, perms, resource, parser
from .. import exceptions
from marshmallow import fields

api = Blueprint('api_agent', __name__, url_prefix='/api/v1/agent')

# Agent Status ********************************************************************************************************
# List agent
@api.route('/find', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'view_agent')
def list_agents():
    """
    List agents
    """
    params = {
        'ossec': fields.Integer(),
        'ossec_log': fields.Integer(),
        'se': fields.Integer(),
        'beat': fields.Integer(),
        'cmd_log': fields.Integer(),
        'oa': fields.Integer(),
        'kav': fields.Integer(),
        'skip': fields.Integer(),
        'ip': fields.String(),
        'group': fields.String(),
        'source': fields.String(),
        'server_id': fields.String(),
        'os': fields.String(),
        'note': fields.String(),
        'connection': fields.Boolean(),
        'connection_data': fields.String(),
        'actor': fields.String(required=True),
        'count': fields.Integer(),
        'since': fields.Integer(),
        'sort': fields.Dict()
    }
    args = parser.parse(params)

    projection = {'_id': 0}
    query = {}

    keys = ['ossec', 'ossec_log', 'se', 'beat', 'cmd_log', 'oa', 'kav', 'skip']
    for k in keys:
        if k in args:
            v = args[k]
            if v:
                query[k] = args[k]
            else:
                query[k] = {'$ne': 1}

    keys = ['ip', 'server_id', 'os', 'note', 'source', 'connection_data']
    for k in keys:
        v = args.get(k, '').strip()
        if v and v != '*':
            query[k] = {'$regex': args[k].strip(), '$options': 'i'}

    group = args.get('group', '')
    if group:
        query['group'] = group

    if 'connection' in args:
        query['connection'] = args['connection']

    sort_key = 'ip'
    sort_value = 1
    if 'sort' in args:
        sort_key = args['sort']['key']
        sort_value = int(args['sort']['value'])

    _sort = [(sort_key, sort_value)]

    data = mongo.db.agents.find(query, projection).sort(_sort)
    count = data.count()

    if 'since' in args:
        data = data.skip(int(args['since']))
    if 'count' in args and args['count'] != -1:
        data = data.limit(int(args['count']))

    result = {'agents': list(data), 'count': count}
    return jsonify(result)


# View an agent
@api.route('/view', methods=['GET'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'view_agent')
def view_agent():
    """
    Xem chi tiêt một agent
    """
    params = {
        'ip': fields.String(),
        'group': fields.String(),
        'actor': fields.String(required=True)
    }
    args = parser.parse(params)

    projection = {'_id': 0}
    query = {
        'ip': args['ip'],
        'group': args['group']
    }

    data = mongo.db.agents.find_one(query, projection)
    if not data:
        raise exceptions.BadRequest(1006)

    return jsonify({'agent': data})


# Add new agent
@api.route('/add', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def add_agent():
    """
    Thêm một Agent mới
    """
    params = {
        'ip': fields.String(required=True),
        'group': fields.String(required=True),
        'source': fields.String(required=True),
        'os': fields.String(),
        'server_id': fields.String(),
        'ossec': fields.Integer(required=True),
        'ossec_log': fields.Integer(required=True),
        'se': fields.Integer(required=True),
        'beat': fields.Integer(required=True),
        'cmd_log': fields.Integer(required=True),
        'oa': fields.Integer(required=True),
        'kav': fields.Integer(required=True),
        'skip': fields.Integer(required=True),
        'note': fields.String(),
        'actor': fields.String(required=True)
    }
    json_data = parser.parse(params)
    ip = json_data['ip'].strip()
    group = json_data['group'].strip()

    data = [row for row in mongo.db.agents.find({'ip': ip, 'group': group})]
    if len(data) > 0:
        raise exceptions.BadRequest(1005, 'Agent IP & Group')

    new_agent = {
        'ip': ip,
        'group': group,
        'source': json_data.get('source', ''),
        'os': json_data.get('os', ''),
        'server_id': json_data.get('server_id', ''),
        'ossec': json_data['ossec'],
        'ossec_log': json_data['ossec_log'],
        'se': json_data['se'],
        'beat': json_data['beat'],
        'cmd_log': json_data['cmd_log'],
        'oa': json_data['oa'],
        'kav': json_data['kav'],
        'skip': json_data['skip'],
        'note': json_data.get('note', '')
    }

    mongo.db.agents.insert(new_agent)
    return jsonify({'ip': ip, 'group': group})


# Edit an agent
@api.route('/edit', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def edit_agent():
    """
    Update an agent
    """
    params = {
        'ip': fields.String(required=True),
        'group': fields.String(required=True),
        'source': fields.String(),
        'os': fields.String(allow_none=True),
        'server_id': fields.String(allow_none=True),
        'ossec': fields.Integer(),
        'ossec_log': fields.Integer(),
        'se': fields.Integer(),
        'beat': fields.Integer(),
        'cmd_log': fields.Integer(),
        'oa': fields.Integer(),
        'kav': fields.Integer(),
        'skip': fields.Integer(),
        'note': fields.String(allow_none=True),
        'actor': fields.String(required=True)
    }
    json_data = parser.parse(params)

    query_params = {
        'ip': json_data['ip'],
        'group': json_data['group']
    }

    data = mongo.db.agents.find_one(query_params)
    if not data:
        raise exceptions.BadRequest(1006)

    update_data = {}
    keys = ['server_id', 'os', 'ossec', 'ossec_log', 'se', 'beat', 'cmd_log', 'oa', 'kav', 'skip', 'note', 'source']
    for k in keys:
        if k in json_data:
            update_data[k] = json_data[k]

    mongo.db.agents.update(query_params, {'$set': update_data})
    return jsonify({'agent': query_params})


# Delete an agent
@api.route('/delete', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def delete_agent():
    """
    Delete an agent
    """
    params = {
        'ip': fields.String(required=True),
        'group': fields.String(required=True),
    }

    json_data = parser.parse(params)

    query_params = {
        'ip': json_data['ip'],
        'group': json_data['group']
    }

    data = mongo.db.agents.find_one(query_params)
    if not data:
        raise exceptions.BadRequest(1006)

    mongo.db.agents.remove(query_params)
    return jsonify({'agent': query_params})


# List of group
@api.route('/groups', methods=['GET'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'view_agent')
def list_groups():
    """
    List groups
    """
    query = {}
    projection = {'_id': 0}
    data = mongo.db.groups.find(query, projection)
    return jsonify({'groups': list(data)})