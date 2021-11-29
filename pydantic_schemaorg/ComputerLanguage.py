from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ComputerLanguage(Intangible):
    """This type covers computer programming languages such as Scheme and Lisp, as well as other"
     "language-like computer representations. Natural languages are best represented"
     "with the [[Language]] type.

    See https://schema.org/ComputerLanguage.

    """

    locals().update({"@type": Field("ComputerLanguage", const=True)})


ComputerLanguage.update_forward_refs()
