import mydatetime_util
from mydatetime import MyDatetime

def test_mydatetime_iso_8601():
    my_datetime = MyDatetime(iso_8601=mydatetime_util.parse_iso_8601("2023-11-13T13:15:32Z"))
    assert my_datetime.iso_8601 == "2023-11-13T13:15:32Z"

def test_mydatetime_to_string():
    my_datetime = MyDatetime(year=2023, month=11, day=13, hour=13, minute=15, second=32)
    assert my_datetime.to_string() == "2023-11-13 13:15:32"

if __name__ == "__main__":
    pytest.main()