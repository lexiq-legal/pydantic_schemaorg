from pydantic import Field
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class Balance(PhysicalActivityCategory):
    """Physical activity that is engaged to help maintain posture and balance.

    See https://schema.org/Balance.

    """
    type_: str = Field("Balance", const=True, alias='@type')
    

Balance.update_forward_refs()
