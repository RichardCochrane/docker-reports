import json

from flask import jsonify, request

from app import app
from app.db import db_session
from app.models import ExerciseSummary
from app.schemas import ExerciseSummarySchema
from marshmallow import ValidationError


def return_non_success_json(status_code, data):
    return app.response_class(
        response=json.dumps(data),
        status=status_code,
        mimetype='application/json'
    )


@app.route('/api/update')
def update_view():
    json_data = request.json
    if not json_data:
        return return_non_success_json(400, {'message': 'No input data provided'})

    # Validate and deserialize input
    summary_schema = ExerciseSummarySchema(only=('created_at', 'subject'))
    try:
        data = summary_schema.load(json_data)
    except ValidationError as err:
        return return_non_success_json(422, err.messages)

    summary = ExerciseSummary(**data.data)
    db_session.add(summary)
    db_session.flush()
    db_session.commit()

    return jsonify({'messages': 'ok'})


@app.route('/api/stats')
def stats_view():
    all_summary = ExerciseSummary.query.all()
    stats = {'total': 0, 'maths': 0, 'science': 0}
    for summary in all_summary:
        stats['total'] += 1
        key = 'maths' if summary.subject == 'maths' else 'science'
        stats[key] += 1

    return jsonify({'data': stats})
