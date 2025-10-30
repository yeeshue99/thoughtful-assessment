import pytest
from PackageSort import sort


class TestSort:
    """Test suite for the package sort function."""

    # Test "Accept" cases - normal packages
    def test_accept_small_package(self):
        """Small package that fits all criteria."""
        assert sort(10, 20, 30, 5) == "Accept"

    def test_accept_at_edge_of_limits(self):
        """Package just under all limits."""
        assert sort(149, 149, 10, 19) == "Accept"

    def test_accept_zero_dimensions(self):
        """Package with zero dimensions (edge case)."""
        assert sort(0, 0, 0, 0) == "Accept"

    # Test "Special" cases - bulky by dimension
    def test_special_bulky_by_width(self):
        """Package is bulky because width exceeds LENGTH_MAX."""
        assert sort(151, 10, 10, 5) == "Special"

    def test_special_bulky_by_height(self):
        """Package is bulky because height exceeds LENGTH_MAX."""
        assert sort(10, 151, 10, 5) == "Special"

    def test_special_bulky_by_length(self):
        """Package is bulky because length exceeds LENGTH_MAX."""
        assert sort(10, 10, 151, 5) == "Special"

    def test_special_bulky_exact_dimension_limit(self):
        """Package is bulky when dimension equals LENGTH_MAX."""
        assert sort(150, 10, 10, 5) == "Special"

    # Test "Special" cases - bulky by volume
    def test_special_bulky_by_volume_exact_limit(self):
        """Package is bulky because volume equals SIZE_MAX."""
        assert sort(100, 100, 100, 5) == "Special"  # 1,000,000

    def test_special_bulky_by_volume_over_limit(self):
        """Package is bulky because volume exceeds SIZE_MAX."""
        assert sort(101, 100, 100, 5) == "Special"  # 1,010,000

    def test_special_bulky_large_volume_small_dimensions(self):
        """Package with no dimension over limit but large volume."""
        assert sort(120, 120, 70, 5) == "Special"  # 1,008,000

    # Test "Special" cases - heavy only
    def test_special_heavy_exact_limit(self):
        """Package is heavy because mass equals WEIGHT_MAX."""
        assert sort(10, 10, 10, 20) == "Special"

    def test_special_heavy_over_limit(self):
        """Package is heavy because mass exceeds WEIGHT_MAX."""
        assert sort(10, 10, 10, 25) == "Special"

    def test_special_very_heavy(self):
        """Package is very heavy."""
        assert sort(10, 10, 10, 1000) == "Special"

    # Test "Reject" cases - both bulky and heavy
    def test_reject_bulky_dimension_and_heavy(self):
        """Package exceeds dimension limit and eight exceeds weight limit."""
        assert sort(200, 10, 10, 25) == "Reject"

    def test_reject_bulky_volume_and_heavy(self):
        """Package equals volume limit and weight equals weight limit."""
        assert sort(100, 100, 100, 20) == "Reject"  # 1,000,000 volume, 20 mass

    def test_reject_all_limits_exceeded(self):
        """Package exceeds all possible limits."""
        assert sort(200, 200, 200, 100) == "Reject"

    def test_reject_exact_both_limits(self):
        """Package at exact limits for both bulky and heavy."""
        assert sort(150, 10, 10, 20) == "Reject"

    # Edge cases
    def test_edge_dimension_at_150(self):
        """Dimension just below LENGTH_MAX (should not be bulky)."""
        assert sort(149, 10, 10, 10) == "Accept"

    def test_edge_mass_at_19(self):
        """Mass just below WEIGHT_MAX (should not be heavy)."""
        assert sort(10, 10, 10, 19) == "Accept"

    def test_edge_volume_just_below_limit(self):
        """Volume just below SIZE_MAX."""
        assert sort(99, 100, 100, 10) == "Accept"  # 990,000

    def test_edge_one_dimension_over_others_ok(self):
        """Only one dimension over limit."""
        assert sort(151, 1, 1, 1) == "Special"

    # Error cases
    def test_error_negative_width(self):
        """Negative width should raise ValueError."""
        with pytest.raises(ValueError,
                           match="All dimensions must be non-negative"):
            sort(-10, 20, 30, 10)

    def test_error_negative_height(self):
        """Negative height should raise ValueError."""
        with pytest.raises(ValueError,
                           match="All dimensions must be non-negative"):
            sort(10, -20, 30, 10)

    def test_error_negative_length(self):
        """Negative length should raise ValueError."""
        with pytest.raises(ValueError,
                           match="All dimensions must be non-negative"):
            sort(10, 20, -30, 10)

    def test_error_negative_mass(self):
        """Negative mass should raise ValueError."""
        with pytest.raises(ValueError,
                           match="All dimensions must be non-negative"):
            sort(10, 20, 30, -10)

    def test_error_all_negative(self):
        """All negative values should raise ValueError."""
        with pytest.raises(ValueError,
                           match="All dimensions must be non-negative"):
            sort(-10, -20, -30, -10)

    # Real-world scenarios
    def test_standard_box(self):
        """Standard shipping box."""
        assert sort(30, 20, 15, 2) == "Accept"

    def test_envelope(self):
        """Flat envelope."""
        assert sort(30, 20, 1, 0.5) == "Accept"

    def test_furniture(self):
        """Large furniture piece."""
        assert sort(180, 80, 60, 15) == "Special"  # bulky by dimension

    def test_heavy_small_item(self):
        """Small but heavy item like metal."""
        assert sort(10, 10, 10, 50) == "Special"  # heavy only

    def test_large_heavy_item(self):
        """Large and heavy item like appliance."""
        assert sort(200, 100, 80, 100) == "Reject"  # both
