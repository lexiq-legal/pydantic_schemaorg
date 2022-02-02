from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """A dry-cleaning business.

    See: https://schema.org/DryCleaningOrLaundry
    Model depth: 4
    """
    type_: str = Field("DryCleaningOrLaundry", alias='@type')
    

