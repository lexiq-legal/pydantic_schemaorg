from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class Preschool(EducationalOrganization):
    """A preschool.

    See https://schema.org/Preschool.

    """

    locals().update({"@type": Field("Preschool", const=True)})


Preschool.update_forward_refs()
