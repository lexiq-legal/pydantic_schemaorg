from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class Preschool(EducationalOrganization):
    """A preschool.

    See https://schema.org/Preschool.

    """
    type_: str = Field("Preschool", const=True, alias='@type')
    

Preschool.update_forward_refs()
