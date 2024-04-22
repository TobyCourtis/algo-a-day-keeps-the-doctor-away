import datetime


def get_data():
    return {
        ("USDGBP", "2022-01-01"): 0.78,
        ("USDGBP", "2022-01-02"): 0.79,
    }


def convert_currency(
        source_currency: str,
        target_currency: str,
        source_amount: float,
        date: datetime.date
):
    key = (f"{source_currency}{target_currency}", date.strftime("%Y-%m-%d"))
    conversion_factor = get_data()[key]
    return conversion_factor * source_amount


assert convert_currency(source_currency="USD",
                        target_currency="GBP",
                        source_amount=1000.0,
                        date=datetime.date(2022, 1, 1)) == 780.0

"""
Practice reversal
"""


def reverse(_list):
    out = []
    for i in range(len(_list) - 1, -1, -1):
        out.append(_list[i])
    return out


def reverse2(_list):
    out = []
    for num in _list:
        out.insert(0, num)
    return out


def reverse3(_list):
    for i in range(len(_list) // 2):
        tmp = _list[i]
        _list[i] = _list[-i - 1]
        _list[-i - 1] = tmp
    return _list


print(reverse([1, 2, 3]))
print(reverse2([1, 2, 3]))
print(reverse3([1, 2, 3, 4]))
print(reverse3([1, 2, 3]))
