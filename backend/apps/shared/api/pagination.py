# Import django
from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    """
    Small pagination
    """
    page_size = 6


class MediumPagination(PageNumberPagination):
    """
    Medium pagination
    """
    page_size = 12


class LargePagination(PageNumberPagination):
    """
    Large pagination
    """
    page_size = 24
