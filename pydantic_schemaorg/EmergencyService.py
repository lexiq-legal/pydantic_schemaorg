from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EmergencyService(LocalBusiness):
    """An emergency service, such as a fire station or ER.

    See https://schema.org/EmergencyService.

    """

    locals().update({"@type": Field("EmergencyService", const=True)})


EmergencyService.update_forward_refs()
