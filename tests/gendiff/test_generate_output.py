import pytest
from gendiff.formatting.stylish import generate_output
from tests.gendiff.fixtures.diffs import AWAITED_DIFFS, AWAITED_NESTED_DIFFS
from tests.gendiff.fixtures.outputs import (
    AWAITED_NESTED_OUTPUTS,
    AWAITED_OUTPUTS,
)


class TestGenerateOutputPlain:
    @pytest.mark.parametrize(
        ("diff_dict", "awaited_diff"),
        [
            pytest.param(
                AWAITED_DIFFS["identical"],
                AWAITED_OUTPUTS["identical"],
                id="identical diff",
            ),
            pytest.param(
                AWAITED_DIFFS["identical"],
                AWAITED_OUTPUTS["identical"],
                id="identical diff",
            ),
            pytest.param(
                AWAITED_DIFFS["missing"],
                AWAITED_OUTPUTS["missing"],
                id="missing diff",
            ),
            pytest.param(
                AWAITED_DIFFS["missing"],
                AWAITED_OUTPUTS["missing"],
                id="missing diff",
            ),
            pytest.param(
                AWAITED_DIFFS["added"],
                AWAITED_OUTPUTS["added"],
                id="added diff",
            ),
            pytest.param(
                AWAITED_DIFFS["changed"],
                AWAITED_OUTPUTS["changed"],
                id="changed diff",
            ),
            pytest.param(
                AWAITED_DIFFS["combined"],
                AWAITED_OUTPUTS["combined"],
                id="combined diff",
            ),
        ],
    )
    def test_generate_diff(
        self,
        diff_dict,
        awaited_diff,
    ):
        diff = generate_output(diff_dict)
        assert diff == awaited_diff


class TestGenerateOutputNested:
    @pytest.mark.parametrize(
        ("diff_dict", "awaited_diff"),
        [
            pytest.param(
                AWAITED_NESTED_DIFFS["identical"],
                AWAITED_NESTED_OUTPUTS["identical"],
                id="identical nested diff",
            ),
            pytest.param(
                AWAITED_NESTED_DIFFS["missing"],
                AWAITED_NESTED_OUTPUTS["missing"],
                id="missing nested diff",
            ),
            pytest.param(
                AWAITED_NESTED_DIFFS["added"],
                AWAITED_NESTED_OUTPUTS["added"],
                id="added nested diff",
            ),
            pytest.param(
                AWAITED_NESTED_DIFFS["changed"],
                AWAITED_NESTED_OUTPUTS["changed"],
                id="changed nested diff",
            ),
            pytest.param(
                AWAITED_NESTED_DIFFS["combined"],
                AWAITED_NESTED_OUTPUTS["combined"],
                id="combined nested diff",
            ),
            pytest.param(
                AWAITED_NESTED_DIFFS["tricky"],
                AWAITED_NESTED_OUTPUTS["tricky"],
                id="tricky nested diff",
            ),
        ],
    )
    def test_generate_diff(
        self,
        diff_dict,
        awaited_diff,
    ):
        diff = generate_output(diff_dict)
        assert diff == awaited_diff
