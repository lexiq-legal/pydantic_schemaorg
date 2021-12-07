from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """A dry-cleaning business.

    See https://schema.org/DryCleaningOrLaundry.

    """
    type_: str = Field("DryCleaningOrLaundry", const=True, alias='@type')
    

DryCleaningOrLaundry.update_forward_refs()
