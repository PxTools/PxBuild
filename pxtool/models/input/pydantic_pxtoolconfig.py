# generated by datamodel-codegen:
#   filename:  pxtoolconfig.yaml
#   timestamp: 2023-09-21T11:25:06+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field, constr


class Admin(BaseModel):
    """
    These properties does not enter the pxfile directly
    """

    valid_languages: List[str] = Field(..., alias='validLanguages')
    """
    The 2-letter languagecodes
    """
    the_word_and: Dict[str, str] = Field(..., alias='theWordAnd')
    the_word_by: Dict[str, str] = Field(..., alias='theWordBy')


class Pxtoolconfig(BaseModel):
    admin: Admin
    """
    These properties does not enter the pxfile directly
    """
    charset: Optional[constr(max_length=20)] = None
    """
    example: ANSI
    """
    axis_version: Optional[constr(max_length=20)] = Field(None, alias='axisVersion')
    """
    Version of px-file format.  example: '2013'
    """
    code_page: Optional[constr(max_length=20)] = Field('iso-8859-1', alias='codePage')
    """
    example: iso-8859-1
    """
    description_default: Optional[bool] = Field(False, alias='descriptionDefault')
    contvariable: Optional[Dict[str, constr(max_length=256)]] = None
    """
    Name for content variable
    """
    contvariable_code: Optional[str] = Field('ContentCode', alias='contvariableCode')
    """
    Code for content variable
    """
    timevariable_code: Optional[str] = Field('Time', alias='timevariableCode')
    """
    Code for the time variable
    """
    datasymbol1: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol2: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol3: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol4: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol5: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol6: Optional[Dict[str, constr(max_length=20)]] = None
    """
    How 1-6 dots in data, are shown on screen
    """
    datasymbol_nil: Optional[Dict[str, constr(max_length=20)]] = Field(
        None, alias='datasymbolNil'
    )
    """
    How stored - are shown on screen
    """
    datasymbol_sum: Optional[Dict[str, constr(max_length=20)]] = Field(
        None, alias='datasymbolSum'
    )
    """
    This if used to indicate how a sum of differing numbers of dots will be shown. The sum is stored as “…….”.
    """
    source: Optional[Dict[str, constr(max_length=256)]] = None
    """
    Name for content variable
    """