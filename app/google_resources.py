from urllib.error import HTTPError
from googleapiclient.discovery import build
from app_logging import logger


class NoUserIdException:
    pass


def get_user_email(credentials):
    with build('oauth2', 'v2', credentials=credentials) as user_info_service:
        try:
            user_info = user_info_service.userinfo().get().execute()
        except HTTPError as e:
            logger.error('Failed to retrieve user info: %s', e)
            raise e

        if user_info and user_info.get('id') and user_info.get('email'):
            return user_info.get('id'), user_info.get('email')
        else:
            raise NoUserIdException()
