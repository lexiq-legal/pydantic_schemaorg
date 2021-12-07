from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class InsuranceAgency(FinancialService):
    """An Insurance agency.

    See https://schema.org/InsuranceAgency.

    """
    type_: str = Field("InsuranceAgency", const=True, alias='@type')
    

InsuranceAgency.update_forward_refs()
