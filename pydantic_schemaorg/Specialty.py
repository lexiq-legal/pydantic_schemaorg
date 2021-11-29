from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class Specialty(Enumeration):
    """Any branch of a field in which people typically develop specific expertise, usually"
     "after significant study, time, and effort.

    See https://schema.org/Specialty.

    """

    locals().update({"@type": Field("Specialty", const=True)})


Specialty.update_forward_refs()
