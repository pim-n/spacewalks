import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    actual_result = text_to_duration("10:20") 
    expected_result = 10.33333333
    assert actual_result == pytest.approx(expected_result)
    
def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations 
    """
    actual_result =  text_to_duration("10:00")
    expected_result = 10
    assert actual_result == expected_result