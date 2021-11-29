from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class AutomatedTeller(FinancialService):
    """ATM/cash machine.

    See https://schema.org/AutomatedTeller.

    """

    locals().update({"@type": Field("AutomatedTeller", const=True)})


AutomatedTeller.update_forward_refs()
