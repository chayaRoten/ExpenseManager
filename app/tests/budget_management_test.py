import pytest
# import interesting


@pytest.mark.skip(reason='not +'
                         '')
def test_add():
    assert interesting.add(1, 2) == 3