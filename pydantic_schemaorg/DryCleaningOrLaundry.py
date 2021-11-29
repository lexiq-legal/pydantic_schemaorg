from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """A dry-cleaning business.

    See https://schema.org/DryCleaningOrLaundry.

    """

    locals().update({"@type": Field("DryCleaningOrLaundry", const=True)})


DryCleaningOrLaundry.update_forward_refs()
