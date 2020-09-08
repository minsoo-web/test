import re


class UserChanger(object):
    def change(self, new_user: str, new_password: str, data: str) -> str:
        data = re.sub('DEFAULT_USER', new_user, data)
        return re.sub('DEFAULT_PASSWORD', new_password, data)
