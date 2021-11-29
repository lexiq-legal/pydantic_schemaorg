from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class BankAccount(FinancialProduct):
    """A product or service offered by a bank whereby one may deposit, withdraw or transfer money"
     "and in some cases be paid interest.

    See https://schema.org/BankAccount.

    """

    accountMinimumInflow: Any = Field(
        None,
        description="A minimum amount that has to be paid in every month.",
    )
    bankAccountType: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="The type of a bank account.",
    )
    accountOverdraftLimit: Any = Field(
        None,
        description="An overdraft is an extension of credit from a lending institution when an account reaches"
     "zero. An overdraft allows the individual to continue withdrawing money even if the account"
     "has no funds in it. Basically the bank allows people to borrow a set amount of money.",
    )
    locals().update({"@type": Field("BankAccount", const=True)})


BankAccount.update_forward_refs()
