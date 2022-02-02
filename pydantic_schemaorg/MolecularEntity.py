from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class MolecularEntity(BioChemEntity):
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical,"
     "radical ion, complex, conformer etc., identifiable as a separately distinguishable"
     "entity.

    See: https://schema.org/MolecularEntity
    Model depth: 3
    """
    type_: str = Field("MolecularEntity", alias='@type')
    iupacName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Systematic method of naming chemical compounds as recommended by the International"
     "Union of Pure and Applied Chemistry (IUPAC).",
    )
    smiles: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A specification in form of a line notation for describing the structure of chemical species"
     "using short ASCII strings. Double bond stereochemistry \ indicators may need to be escaped"
     "in the string in formats where the backslash is an escape character.",
    )
    molecularWeight: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        None,
        description="This is the molecular weight of the entity being described, not of the parent. Units should"
     "be included in the form '&lt;Number&gt; &lt;unit&gt;', for example '12 amu' or as '&lt;QuantitativeValue&gt;.",
    )
    inChI: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Non-proprietary identifier for molecular entity that can be used in printed and electronic"
     "data sources thus enabling easier linking of diverse data compilations.",
    )
    molecularFormula: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The empirical formula is the simplest whole number ratio of all the atoms in a molecule.",
    )
    chemicalRole: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        None,
        description="A role played by the BioChemEntity within a chemical context.",
    )
    inChIKey: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="InChIKey is a hashed version of the full InChI (using the SHA-256 algorithm).",
    )
    monoisotopicMolecularWeight: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        None,
        description="The monoisotopic mass is the sum of the masses of the atoms in a molecule using the unbound,"
     "ground-state, rest mass of the principal (most abundant) isotope for each element instead"
     "of the isotopic average mass. Please include the units the form '&lt;Number&gt; &lt;unit&gt;',"
     "for example '770.230488 g/mol' or as '&lt;QuantitativeValue&gt;.",
    )
    potentialUse: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        None,
        description="Intended use of the BioChemEntity by humans.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
