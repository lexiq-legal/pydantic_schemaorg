from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c3(USNonprofitType):
    """Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable,"
     "Scientific, Literary, Testing for Public Safety, to Foster National or International"
     "Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations.

    See https://schema.org/Nonprofit501c3.

    """

    locals().update({"@type": Field("Nonprofit501c3", const=True)})


Nonprofit501c3.update_forward_refs()
