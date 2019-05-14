class APIError(Exception):
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    """自定义输入错误或无效值"""

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:not found', field, message)


class APIPermissionError(APIError):
    """无权限"""

    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)


class Page(object):
    def __init__(self, item_count, page_index=1, page_size=10):
        self.item_count = item_count
        self.page_size = page_size
        self.page_count = item_count
        if (item_count == 0) or (page_index > self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index
            self.offset = self.page_size * (page_index - 1)
            self.limit = self.page_size
        self.has_next = self.page_index < self.page_count
        self.has_previous = self.page_index > 1

    def __str__(self):
        return 'item_count: %s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s' % (
        self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit)

    __repr__ = __str__


class Response(object):
    def __init__(self, code=0, message="", data=None):
        self.code = code
        self.message = message
        self.data = data

    @staticmethod
    def SUCCESS():
        return Response(code=0, message='success')

    @staticmethod
    def ERROR():
        return Response(code=-1, message='error')

    @staticmethod
    def error(message='', code=-1):
        return Response(code=code, message=message)

    @staticmethod
    def success(data=None):
        return Response(code=0, message='success', data=data)

    @staticmethod
    def NO_AUTH():
        return Response(code=403, message='no auth', data=None)

