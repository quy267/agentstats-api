__author__ = 'huydq17'
from flask import Blueprint, jsonify, request, abort
from ..extensions import mongo, perms, resource, parser
from .. import exceptions
from marshmallow import fields

api = Blueprint('api_account', __name__, url_prefix='/api/v1/account')


@api.route('/find', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'view_agent')
def list_accounts():
    """
    List accounts
    """
    params = {
        'account_number': fields.Integer(),
        'balance': fields.Integer(),
        'firstname': fields.String(),
        'lastname': fields.String(),
        'age': fields.Integer(),
        'gender': fields.Boolean(),
        'address': fields.String(),
        'employer': fields.String(),
        'email': fields.String(),
        'city': fields.String(),
        'state': fields.String(),
        'actor': fields.String(required=True),
        'count': fields.Integer(),
        'since': fields.Integer(),
        'sort': fields.Dict()
    }

    args = parser.parse(params)
    projection = {'_id': 0}
    query = {}

    keys = ['account_number', 'balance', 'age']
    for k in keys:
        if k in args:
            v = args[k]
            if v:
                query[k] = args[k]
            else:
                query[k] = {'$ne': 1}

    keys = ['firstname', 'lastname', 'gender', 'address', 'employer', 'email', 'city', 'state']
    for k in keys:
        v = args.get(k, '').strip()
        if v and v != '*':
            query[k] = {'$regex': args[k].strip(), '$options': 'i'}

    if 'gender' in args:
        query['gender'] = args['gender']

    sort_key = 'account_number'
    sort_value = 1
    if 'sort' in args:
        sort_key = args['sort']['key']
        sort_value = int(args['sort']['value'])

    _sort = [(sort_key, sort_value)]

    data = mongo.db.accounts.find(query, projection).sort(_sort)
    count = data.count()

    if 'since' in args:
        data = data.skip(int(args['since']))
    if 'count' in args and args['count'] != -1:
        data = data.limit(int(args['count']))

    result = {'accounts': list(data), 'count': count}
    return jsonify(result)


# View an account
@api.route('/view', methods=['GET'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'view_agent')
def view_account():
    """
    Xem chi tiet mot angent
    :return:
    """
    params = {
        'account_number': fields.String(),
        'actor': fields.String(required=True)
    }

    args = parser.parse(params)

    projection = {'_id': 0}

    query = {
        'account_number': args['account_number'],
    }

    data = mongo.db.accounts.find_one(query, projection)
    if not data:
        raise exceptions.BadRequest(1006)

    return jsonify({'account': data})


# Add new account
@api.route('/add', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def add_account():
    """
    Them mot account moi
    :return:
    """
    params = {
        'account_number': fields.Integer(required=True),
        'balance': fields.Integer(required=True),
        'firstname': fields.String(required=True),
        'lastname': fields.String(required=True),
        'age': fields.Integer(required=True),
        'gender': fields.Boolean(required=True),
        'address': fields.String(required=True),
        'employer': fields.String(required=True),
        'email': fields.String(required=True),
        'city': fields.String(required=True),
        'state': fields.String(required=True),
        'actor': fields.String(required=True)
    }
    json_data = parser.parse(params)
    account_number = json_data['account_number']
    data = [row for row in mongo.db.agents.find({'account_number': account_number})]
    if len(data) > 0:
        raise exceptions.BadRequest(1005, 'account_number')

    new_account = {
        'account_number': account_number,
        'balance': json_data['balance'],
        'firstname': json_data.get('firstname', ''),
        'lastname': json_data.get('lastname', ''),
        'age': json_data['age'],
        'gender': json_data['gender'],
        'address': json_data.get('address', ''),
        'employer': json_data.get('employer', ''),
        'email': json_data.get('email', ''),
        'city': json_data.get('city', ''),
        'state': json_data.get('state', '')
    }

    mongo.db.agents.insert(new_account)
    return jsonify({'account_number': account_number})


# Edit an account
@api.route('/edit', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def edit_account():
    """
    Update an account
    :return:
    """
    params = {
        'account_number': fields.Integer(required=True),
        'balance': fields.Integer(required=True),
        'firstname': fields.String(),
        'lastname': fields.String(),
        'age': fields.Integer(),
        'gender': fields.Boolean(),
        'address': fields.String(),
        'employer': fields.String(),
        'email': fields.String(),
        'city': fields.String(),
        'state': fields.String(),
        'actor': fields.String(required=True)
    }

    json_data = parser.parse(params)

    query_params = {
        'account_number': json_data['account_number'],
        'balance': json_data['balance'],

    }

    data = mongo.db.accounts.find_one(query_params)
    if not data:
        raise exceptions.BadRequest(1006)

    update_data = {}
    keys = ['balance', 'firstname', 'lastname', 'age', 'gender', 'address', 'employer', 'email', 'city', 'state']
    for k in keys:
        if k in json_data:
            update_data[k] = json_data[k]

    mongo.db.accounts.update(query_params, {'$set': update_data})
    return jsonify({'account': query_params})


# Delete an account
@api.route('/delete', methods=['POST'])
@resource.require_oauth('agentstats')
@perms.require_perm('agentstats', 'edit_agent')
def delete_account():
    """
    Delete an account
    :return:
    """
    params = {
        'account_number': fields.Integer(required=True)
    }

    json_data = parser.parse(params)

    query_params = {
        'account_number': json_data['account_number'],

    }

    data = mongo.db.accounts.find_one(query_params)
    if not data:
        raise exceptions.BadRequest(1006)

    mongo.db.accounts.remove(query_params)
    return jsonify({'account': query_params})
