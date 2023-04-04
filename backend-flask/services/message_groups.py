from datetime import datetime, timedelta, timezone

from lib.ddb import Ddb
from lib.db import db

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
# cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
logger.addHandler(console_handler)
# logger.addHandler(cw_handler)

class MessageGroups:
    @staticmethod
    def run(cognito_user_id):
        model = {
            'errors': None,
            'data': None
        }

        sql = db.template('users', 'uuid_from_cognito_user_id')
        my_user_uuid = db.query_value(sql, {
            'cognito_user_id': cognito_user_id
        })
        logger.debug(f"UUID: {my_user_uuid}")

        ddb = Ddb.client()
        data = Ddb.list_message_groups(ddb, my_user_uuid)
        logger.debug(f"list_message_groups: {data}")

        model['data'] = data
        return model
