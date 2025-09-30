import pytest
from presidio_anonymizer.sample import sample_run_anonymizer
@pytest.mark.parametrize(
        "text, start, end, dictExpected",
        [
            ("My name is Bond.",11,15,{'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'})
        ],
)
def test_sample_run_anonymizer(text, start, end, dictExpected):
    result  = sample_run_anonymizer(text,start,end)
    dict = result.items[0]
    dict = {
        "start": dict.start,
        "end": dict.end,
        "text": dict.text,
        "entity_type": dict.entity_type,
        "operator": dict.operator
    }
    assert dictExpected == dict
   