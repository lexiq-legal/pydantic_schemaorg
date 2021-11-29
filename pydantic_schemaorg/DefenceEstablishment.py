from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class DefenceEstablishment(GovernmentBuilding):
    """A defence establishment, such as an army or navy base.

    See https://schema.org/DefenceEstablishment.

    """

    locals().update({"@type": Field("DefenceEstablishment", const=True)})


DefenceEstablishment.update_forward_refs()
