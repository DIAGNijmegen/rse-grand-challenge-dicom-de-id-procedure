from enum import Enum


class ActionChoices(str, Enum):
    REMOVE = "X"
    KEEP = "K"

    REPLACE = "D"
    REPLACE_0 = "Z"
    UID = "U"

    REJECT = "R"


All_ACTION_CHOICES = {a.value for a in ActionChoices}
