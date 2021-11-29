from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class RestrictedDiet(Enumeration):
    """A diet restricted to certain foods or preparations for cultural, religious, health"
     "or lifestyle reasons.

    See https://schema.org/RestrictedDiet.

    """

    locals().update({"@type": Field("RestrictedDiet", const=True)})


RestrictedDiet.update_forward_refs()
