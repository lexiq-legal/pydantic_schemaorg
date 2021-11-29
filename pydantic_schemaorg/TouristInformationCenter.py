from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TouristInformationCenter(LocalBusiness):
    """A tourist information center.

    See https://schema.org/TouristInformationCenter.

    """

    locals().update({"@type": Field("TouristInformationCenter", const=True)})


TouristInformationCenter.update_forward_refs()
