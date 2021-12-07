from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class BankOrCreditUnion(FinancialService):
    """Bank or credit union.

    See https://schema.org/BankOrCreditUnion.

    """
    type_: str = Field("BankOrCreditUnion", const=True, alias='@type')
    

BankOrCreditUnion.update_forward_refs()
