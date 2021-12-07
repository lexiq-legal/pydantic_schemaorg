from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class SchoolDistrict(AdministrativeArea):
    """A School District is an administrative area for the administration of schools.

    See https://schema.org/SchoolDistrict.

    """
    type_: str = Field("SchoolDistrict", const=True, alias='@type')
    

SchoolDistrict.update_forward_refs()
