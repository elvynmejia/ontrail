from tests.test_base import TestBase
from actions.error import ActionErrorBase


class TestActionErrorBase(TestBase):
    def test_list_or_errors_items_is_a_dict(self):
        errors = ActionErrorBase(
            errors=[{"id": ["Must not be null"], "title": ["Must not be null"]}]
        ).as_json()

        assert len(errors["errors"]) == 2
        assert isinstance(errors["errors"][0]["id"], list)
        assert isinstance(errors["errors"][1]["title"], list)
