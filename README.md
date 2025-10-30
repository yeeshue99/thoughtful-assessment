# Package Sort

Package classification tool for Thoughtful

Overview
- Classification logic is implemented in [`PackageSort.py`](PackageSort.py) as the function [`PackageSort.sort`](PackageSort.py).
- Unit tests live in [`test_PackageSort.py`](test_PackageSort.py).
- Small demo runner is in [`main.py`](main.py).

Behavior
- A package is considered bulky if any dimension >= [`PackageSort.LENGTH_MAX`](PackageSort.py) or if its volume
  $V = width \times height \times length$ satisfies $V \ge$ [`PackageSort.SIZE_MAX`](PackageSort.py).
- A package is considered heavy if mass $\ge$ [`PackageSort.WEIGHT_MAX`](PackageSort.py).
- The function [`PackageSort.sort`](PackageSort.py) returns one of:
  - `"Accept"` — neither bulky nor heavy
  - `"Special"` — bulky xor heavy
  - `"Reject"` — both bulky and heavy
- Negative inputs raise `ValueError` (see tests in [`test_PackageSort.py`](test_PackageSort.py)).
- Dimensions are in cm units and weight is in kg units.

Key constants
- [`PackageSort.SIZE_MAX`](PackageSort.py) = 1000000
- [`PackageSort.LENGTH_MAX`](PackageSort.py) = 150
- [`PackageSort.WEIGHT_MAX`](PackageSort.py) = 20

Quick start

Run the demo:
```sh
python [main.py](http://_vscodecontentref_/0)```