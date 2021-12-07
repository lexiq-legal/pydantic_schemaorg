from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class ElementarySchool(EducationalOrganization):
    """An elementary school.

    See https://schema.org/ElementarySchool.

    """
    type_: str = Field("ElementarySchool", const=True, alias='@type')
    

ElementarySchool.update_forward_refs()
