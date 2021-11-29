from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """A general contractor.

    See https://schema.org/GeneralContractor.

    """

    locals().update({"@type": Field("GeneralContractor", const=True)})


GeneralContractor.update_forward_refs()
