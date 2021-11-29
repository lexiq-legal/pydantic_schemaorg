from pydantic import Field
from pydantic_schema_org.CreativeWork import CreativeWork
from pydantic_schema_org.ListItem import ListItem


class HowToTip(CreativeWork, ListItem):
    """An explanation in the instructions for how to achieve a result. It provides supplementary"
     "information about a technique, supply, author's preference, etc. It can explain what"
     "could be done, or what should not be done, but doesn't specify what should be done (see"
     "HowToDirection).

    See https://schema.org/HowToTip.

    """

    locals().update({"@type": Field("HowToTip", const=True)})


HowToTip.update_forward_refs()
