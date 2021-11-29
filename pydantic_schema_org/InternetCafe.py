from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class InternetCafe(LocalBusiness):
    """An internet cafe.

    See https://schema.org/InternetCafe.

    """

    locals().update({"@type": Field("InternetCafe", const=True)})


InternetCafe.update_forward_refs()
