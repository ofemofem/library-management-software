from rest_framework import pagination
from rest_framework.response import Response


class BasePagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):

        return Response({
            'pagination': {
                'total': self.page.paginator.count,
                'per_page': self.page_size,
                'current': self.page.number
            },
            'results': data
        })
