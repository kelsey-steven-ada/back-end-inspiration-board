from flask import jsonify, abort, make_response

def error_message(message, status_code):
    abort(
        make_response(
            jsonify(dict(details=message)
        ), status_code)
    )

def make_class_safely(cls, data_dict):
    try:
        return cls.from_dict(data_dict)
    except KeyError as err:
        error_message(f"Missing key: {err}", 400)

def get_record_by_id(cls, id):
    try:
        id = int(id)
    except ValueError:
        error_message(f"Invalid id {id}", 400)

    record = cls.query.get(id)
    if record:
        return record

    error_message(f"No record of type {cls} with id {id} found", 404)