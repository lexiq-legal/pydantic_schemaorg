from pydantic import Field
from pydantic_schema_org.EntertainmentBusiness import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """An adult entertainment establishment.

    See https://schema.org/AdultEntertainment.

    """

    locals().update({"@type": Field("AdultEntertainment", const=True)})


AdultEntertainment.update_forward_refs()
