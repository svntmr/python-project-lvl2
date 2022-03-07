import pytest
from gendiff.formatting.plain import generate_output as plain_output
from tests.gendiff.fixtures.diffs import EXPECTED_DIFFS
from tests.gendiff.fixtures.outputs import EXPECTED_OUTPUTS


class TestPlainOutput:
    @pytest.mark.parametrize(
        ("diff_dict", "awaited_diff"),
        [
            pytest.param(
                EXPECTED_DIFFS["plain"]["identical"],
                EXPECTED_OUTPUTS["plain"]["plain"]["identical"],
                id="identical diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["plain"]["missing"],
                EXPECTED_OUTPUTS["plain"]["plain"]["missing"],
                id="missing diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["plain"]["added"],
                EXPECTED_OUTPUTS["plain"]["plain"]["added"],
                id="added diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["plain"]["changed"],
                EXPECTED_OUTPUTS["plain"]["plain"]["changed"],
                id="changed diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["plain"]["combined"],
                EXPECTED_OUTPUTS["plain"]["plain"]["combined"],
                id="combined diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["nested"]["identical"],
                EXPECTED_OUTPUTS["plain"]["nested"]["identical"],
                id="identical nested diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["nested"]["missing"],
                EXPECTED_OUTPUTS["plain"]["nested"]["missing"],
                id="missing nested diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["nested"]["added"],
                EXPECTED_OUTPUTS["plain"]["nested"]["added"],
                id="added nested diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["nested"]["changed"],
                EXPECTED_OUTPUTS["plain"]["nested"]["changed"],
                id="changed nested diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["nested"]["combined"],
                EXPECTED_OUTPUTS["plain"]["nested"]["combined"],
                id="combined nested diff",
            ),
            pytest.param(
                EXPECTED_DIFFS["nested"]["tricky"],
                EXPECTED_OUTPUTS["plain"]["nested"]["tricky"],
                id="tricky nested diff",
            ),
        ],
    )
    def test_generate_diff(self, diff_dict, awaited_diff):
        diff = plain_output(diff_dict)
        assert diff == awaited_diff
