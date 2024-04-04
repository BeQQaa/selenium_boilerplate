import pytest


@pytest.fixture(params=[
    (1, 2, 3),
    (5, 5, 10),
    (10, -5, 5)
])
def addition_params(request):
    return request.param
