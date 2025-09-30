import pytest
from presidio_anonymizer.sample import sample_run_anonymizer
@pytest.mark.parametrize(
        "text, start, end",
        [
            ("My name is Bond.",11,15)
        ],
)
def test_sample_run_anonymizer(text, start, end):
    assert sample_run_anonymizer(text,start,end)