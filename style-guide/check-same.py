# -*- coding: utf-8 -*-
"""Impersonal pronoun same."""

from proselint.tools import existence_check, memoize


@memoize
def check_same(text):
    """Check Impersonal pronoun same."""
    err = "style-guide.check-same"
    msg = "Avoid using \"The same\"."
    regex = "\. The same"

    return existence_check(text, [regex], err, msg, ignore_case=False, 
    	                   require_padding=False)

