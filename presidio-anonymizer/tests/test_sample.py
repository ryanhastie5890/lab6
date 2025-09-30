import pytest
from presidio_anonymizer.sample import sample_run_anonymizer
@pytest.mark.parametrize(
        "text, start, end, dictExpected, textExpected",
        [
            ("My name is Bond.",11,15,{'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}, "My name is BIP.")
        ],
)
def test_sample_run_anonymizer(text, start, end, dictExpected, textExpected):
    result  = sample_run_anonymizer(text,start,end)
    dict = result.items[0]
    dict = {
        "start": dict.start,
        "end": dict.end,
        "text": dict.text,
        "entity_type": dict.entity_type,
        "operator": dict.operator
    }
    assert result.text == textExpected
    assert len(result.items) == 1
    assert result.items[0].start == dictExpected["start"]
    assert result.items[0].end == dictExpected["end"]
    
   