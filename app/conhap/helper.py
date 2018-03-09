from flask import make_response, jsonify, url_for
from app import app
from app.models import Conapp


def response_for_user_conhap(user_conhap):
    """
    Return the response for when a single conhap when requested by the user.
    :param user_conhap:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'conhap': user_conhap
    }))


def response_for_created_conhap(user_conhap, status_code):
    """
    Method returning the response when a conhap has been successfully created.
    :param status_code:
    :param user_conhap: conhap
    :return: Http Response
    """
    return make_response(jsonify({
        'status': 'success',
        'id': user_conhap.id,
        'name': user_conhap.name,
        'createdAt': user_conhap.create_at,
        'modifiedAt': user_conhap.modified_at
    })), status_code


def response(status, message, code):
    """
    Helper method to make a http response
    :param status: Status message
    :param message: Response message
    :param code: Response status code
    :return: Http Response
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), code


def get_user_conhap_json_list(user_conhaps):
    """
    Make json objects of the user conhaps and add them to a list.
    :param user_conhaps: conhap
    :return:
    """
    conhaps = []
    for user_conhap in user_conhaps:
        conhaps.append(user_conhap.json())
    return conhaps


def response_with_pagination(conhaps, previous, nex, count):
    """
    Make a http response for conhapList get requests.
    :param count: Pagination Total
    :param nex: Next page Url if it exists
    :param previous: Previous page Url if it exists
    :param conhaps: conhap
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': 'success',
        'previous': previous,
        'next': nex,
        'count': count,
        'conhaps': conhaps
    })), 200


def paginate_conhaps(user_id, page, q, user):
    """
    Get a user by Id, then get hold of their conhaps and also paginate the results.
    There is also an option to search for a conhap name if the query param is set.
    Generate previous and next pagination urls
    :param q: Query parameter
    :param user_id: User Id
    :param user: Current User
    :param page: Page number
    :return: Pagination next url, previous url and the user conhaps.
    """
    if q:
        pagination = conhap.query.filter(conhap.name.like("%" + q.lower().strip() + "%")).filter_by(user_id=user_id) \
            .paginate(page=page, per_page=app.config['conhap_AND_ITEMS_PER_PAGE'], error_out=False)
    else:
        pagination = user.conhaps.paginate(page=page, per_page=app.config['conhap_AND_ITEMS_PER_PAGE'],
                                           error_out=False)
    previous = None
    if pagination.has_prev:
        if q:
            previous = url_for('conhap.conhaplist', q=q, page=page - 1, _external=True)
        else:
            previous = url_for('conhap.conhaplist', page=page - 1, _external=True)
    nex = None
    if pagination.has_next:
        if q:
            nex = url_for('conhap.conhaplist', q=q, page=page + 1, _external=True)
        else:
            nex = url_for('conhap.conhaplist', page=page + 1, _external=True)
    items = pagination.items
    return items, nex, pagination, previous
