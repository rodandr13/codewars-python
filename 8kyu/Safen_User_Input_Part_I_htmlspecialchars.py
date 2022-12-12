"""
Mission
Your mission is to implement a function that converts the
following potentially harmful characters:

< --> &lt;
> --> &gt;
" --> &quot;
& --> &amp;

"""


def html_special_chars(data):
    symbols = "&<>\""
    safe_symbols = ("&amp;", "&lt;", "&gt;", "&quot;")
    for i, symbol in enumerate(symbols):
        data = data.replace(symbols[i], safe_symbols[i])
    return data

