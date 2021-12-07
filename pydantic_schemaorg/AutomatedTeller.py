from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class AutomatedTeller(FinancialService):
    """ATM/cash machine.

    See https://schema.org/AutomatedTeller.

    """
    type_: str = Field("AutomatedTeller", const=True, alias='@type')
    

AutomatedTeller.update_forward_refs()
