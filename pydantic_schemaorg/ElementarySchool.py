from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class ElementarySchool(EducationalOrganization):
    """An elementary school.

    See https://schema.org/ElementarySchool.

    """

    locals().update({"@type": Field("ElementarySchool", const=True)})


ElementarySchool.update_forward_refs()
