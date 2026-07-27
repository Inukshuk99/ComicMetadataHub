"""
ComicMetadataHub Field Rules Test
"""


import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.hub.rules.field_rules import (
    FieldRules
)



def test_field_rules():

    print(
        "Testing field rules..."
    )


    rules = FieldRules()


    assert rules.get_rule(
        "title"
    ) == "review"


    assert rules.get_rule(
        "publisher"
    ) == "priority"


    assert rules.get_rule(
        "unknown"
    ) == "default"


    print(
        "Field rules test passed"
    )



if __name__ == "__main__":

    test_field_rules()
