from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class Embassy(GovernmentBuilding):
    """An embassy.

    See https://schema.org/Embassy.

    """

    locals().update({"@type": Field("Embassy", const=True)})


Embassy.update_forward_refs()
