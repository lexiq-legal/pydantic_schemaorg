from pydantic import Field
from pydantic_schema_org.Store import Store


class PawnShop(Store):
    """A shop that will buy, or lend money against the security of, personal possessions.

    See https://schema.org/PawnShop.

    """

    locals().update({"@type": Field("PawnShop", const=True)})


PawnShop.update_forward_refs()
