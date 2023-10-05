import pytest
from pydantic import ValidationError
from random import random, randint
from faker import Faker


def get_valid_range():
    res = [
        (0.0, 1.0),
        (-0.1, 1.0),
        (0.0, 1.1),
    ]
    a, b = random(), random()
    if a > b:
        res.append((b, a))
    else:
        res.append((a, b))
    return res


def get_invalid_range():
    res = [
        (0.0, "0.5'+OR+1=1--"),
        ("0.0'+OR+1=1--", 0.99),
        ('', ''),
        ('', ' '),
        (' ', ''),
        (' ', ' '),
        ('$#%^$', '')
    ]
    faker = Faker(locale='en')
    res.append((faker.word(), faker.word()))
    res.append((faker.word(), 1.0))
    res.append((0.0, faker.word()))
    a = random() + randint(1, 10)
    b = random() + randint(2, 10)
    res.append((a, b))
    res.append((-1*b, -1*a))
    return res


@pytest.mark.parametrize('accessibility_range', get_valid_range())
def test_find_activity_by_valid_accessibility_range(get_random_activity_by_accessibility_range, accessibility_range):
    try:
        get_random_activity_by_accessibility_range.assert_status_code([200, 404]).valid()
    except ValidationError:
        get_random_activity_by_accessibility_range.check_no_activity_found()


@pytest.mark.parametrize('accessibility_range', get_invalid_range())
def test_find_activity_by_invalid_accessibility_range(get_random_activity_by_accessibility_range, accessibility_range):
    get_random_activity_by_accessibility_range.check_wrong_query_arguments_error()
