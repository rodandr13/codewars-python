"""
Yup, fill the provided set with the keywords of your language.

The test provides the number of needed keywords, and the error messages contain
hints if you need help.

Details:
Keywords are the words put aside as instructions for the compiler. For example
(use these to get started):
if True nonlocal
If your language has contextual or "soft" keywords, you won't find them here.
Only keywords that are always recognized are included.
The example test case will only check your list length.
The keywords should be strings.
"""


import keyword

keywords = set(keyword.kwlist)

