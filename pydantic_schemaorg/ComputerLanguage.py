from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ComputerLanguage(Intangible):
    """This type covers computer programming languages such as Scheme and Lisp, as well as other"
     "language-like computer representations. Natural languages are best represented"
     "with the [[Language]] type.

    See: https://schema.org/ComputerLanguage
    Model depth: 3
    """
    type_: str = Field("ComputerLanguage", alias='@type')
    

