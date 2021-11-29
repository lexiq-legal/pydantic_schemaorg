from pydantic import Field
from pydantic_schemaorg.LoanOrCredit import LoanOrCredit
from pydantic_schemaorg.PaymentCard import PaymentCard


class CreditCard(LoanOrCredit, PaymentCard):
    """A card payment method of a particular brand or name. Used to mark up a particular payment"
     "method and/or the financial product/service that supplies the card account. Commonly"
     "used values: * http://purl.org/goodrelations/v1#AmericanExpress * http://purl.org/goodrelations/v1#DinersClub"
     "* http://purl.org/goodrelations/v1#Discover * http://purl.org/goodrelations/v1#JCB"
     "* http://purl.org/goodrelations/v1#MasterCard * http://purl.org/goodrelations/v1#VISA

    See https://schema.org/CreditCard.

    """

    locals().update({"@type": Field("CreditCard", const=True)})


CreditCard.update_forward_refs()
