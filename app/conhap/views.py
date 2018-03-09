from flask import Blueprint, request, abort
from app.auth.helper import token_required
from app.conhap.helper import response, response_for_created_conhap, response_for_user_conhap, response_with_pagination, \
    get_user_conhap_json_list, paginate_conhaps
from app.models import User, conhap

# Initialize blueprint
conhap = Blueprint('conhap', __name__)


@conhap.route('/conhaplists/', methods=['GET'])
@token_required
def conhaplist(current_user):
    """
    Return all the conhaps owned by the user or limit them to 10.
    Return an empty conhaps object if user has no conhaps
    :param current_user:
    :return:
    """
    user = User.get_by_id(current_user.id)
    page = request.args.get('page', 1, type=int)
    q = request.args.get('q', None, type=str)

    items, nex, pagination, previous = paginate_conhaps(current_user.id, page, q, user)

    if items:
        return response_with_pagination(get_user_conhap_json_list(items), previous, nex, pagination.total)
    return response_with_pagination([], previous, nex, 0)


@conhap.route('/conhaplists/', methods=['POST'])
@token_required
def create_conhaplist(current_user):
    """
    Create a conhap from the sent json data.
    :param current_user: Current User
    :return:
    """
    if request.content_type == 'application/json':
        data = request.get_json()
        name = data.get('name')
        if name:
            user_conhap = conhap(name.lower(), current_user.id)
            user_conhap.save()
            return response_for_created_conhap(user_conhap, 201)
        return response('failed', 'Missing name attribute', 400)
    return response('failed', 'Content-type must be json', 202)


@conhap.route('/conhaplists/<conhap_id>', methods=['GET'])
@token_required
def get_conhap(current_user, conhap_id):
    """
    Return a user conhap with the supplied user Id.
    :param current_user: User
    :param conhap_id: conhap Id
    :return:
    """
    try:
        int(conhap_id)
    except ValueError:
        return response('failed', 'Please provide a valid conhap Id', 400)
    else:
        user_conhap = User.get_by_id(current_user.id).conhaps.filter_by(id=conhap_id).first()
        if user_conhap:
            return response_for_user_conhap(user_conhap.json())
        return response('failed', "conhap not found", 404)


@conhap.route('/conhaplists/<conhap_id>', methods=['PUT'])
@token_required
def edit_conhap(current_user, conhap_id):
    """
    Validate the conhap Id. Also check for the name attribute in the json payload.
    If the name exists update the conhap with the new name.
    :param current_user: Current User
    :param conhap_id: conhap Id
    :return: Http Json response
    """
    if request.content_type == 'application/json':
        data = request.get_json()
        name = data.get('name')
        if name:
            try:
                int(conhap_id)
            except ValueError:
                return response('failed', 'Please provide a valid conhap Id', 400)
            user_conhap = User.get_by_id(current_user.id).conhaps.filter_by(id=conhap_id).first()
            if user_conhap:
                user_conhap.update(name)
                return response_for_created_conhap(user_conhap, 201)
            return response('failed', 'The conhap with Id ' + conhap_id + ' does not exist', 404)
        return response('failed', 'No attribute or value was specified, nothing was changed', 400)
    return response('failed', 'Content-type must be json', 202)


@conhap.route('/conhaplists/<conhap_id>', methods=['DELETE'])
@token_required
def delete_conhap(current_user, conhap_id):
    """
    Deleting a User conhap from the database if it exists.
    :param current_user:
    :param conhap_id:
    :return:
    """
    try:
        int(conhap_id)
    except ValueError:
        return response('failed', 'Please provide a valid conhap Id', 400)
    user_conhap = User.get_by_id(current_user.id).conhaps.filter_by(id=conhap_id).first()
    if not user_conhap:
        abort(404)
    user_conhap.delete()
    return response('success', 'conhap Deleted successfully', 200)


@conhap.errorhandler(404)
def handle_404_error(e):
    """
    Return a custom message for 404 errors.
    :param e:
    :return:
    """
    return response('failed', 'conhap resource cannot be found', 404)


@conhap.errorhandler(400)
def handle_400_errors(e):
    """
    Return a custom response for 400 errors.
    :param e:
    :return:
    """
    return response('failed', 'Bad Request', 400)
