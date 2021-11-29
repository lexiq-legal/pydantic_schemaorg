from pydantic import Field
from pydantic_schema_org.GovernmentBuilding import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """A courthouse.

    See https://schema.org/Courthouse.

    """

    locals().update({"@type": Field("Courthouse", const=True)})


Courthouse.update_forward_refs()
