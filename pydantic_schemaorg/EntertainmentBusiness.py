from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """A business providing entertainment.

    See https://schema.org/EntertainmentBusiness.

    """
    type_: str = Field("EntertainmentBusiness", const=True, alias='@type')
    

EntertainmentBusiness.update_forward_refs()
