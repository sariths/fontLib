"""
Use the function createJsonFile to update fontNames.json in the root directory.
"""
from fontTools import ttLib
import os
import json

def __extractFontName(font, FONT_SPECIFIER_NAME_ID = 4, FONT_SPECIFIER_FAMILY_ID = 1):
    """

    :param font: An instance of the class ttlib.TTFont
    :type font: ttLib.TTFont
    :param FONT_SPECIFIER_NAME_ID: Defaults to 4
    :param FONT_SPECIFIER_FAMILY_ID: Defaults to 1
    :return: A tuple containing the name of the font and the family of the font.

    Usage:
        ttfFile=someFont.tff
        tt=ttLib.TTFont(ttfFile)
        name,family=shortname(tt)

    This function was mostly copied from an existing code snippet on github. Credit to
    the original author.
    """
    name = ""
    family = ""
    for record in font['name'].names:
        if b'\x00' in record.string:
            name_str = record.string.decode('utf-16-be')
        else:
            try:
                name_str = record.string.decode('utf-8')
            except UnicodeDecodeError:
                name_str = record.string.decode('latin-1')
        if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
            name = name_str
        elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
            family = name_str
        if name and family: break
    return name, family


def createJsonFile(jsonPath="fontNames.json",fontDirectory="fonts"):
    """

    :param jsonPath: Path where the json file is to be written.
    :param fontDirectory: The directory where the fonts are stored.
    :return:

    Instead of storing absolute or relative paths, I am storing the directory and the
    fontfiles as two separate entries in the json.
    """

    abbDict={"narrow":"Nar","italic":"Ita","bold":"Bld","regular":"Reg","style":"",
             "condensed":"Cnd","light":"Lig"}

    outputDict={}
    outputDict["directory"]=fontDirectory
    outputDict["fonts"]={}
    for idx,fileType in enumerate(os.listdir(fontDirectory)):
        fileName=os.path.join(fontDirectory,fileType)
        if os.path.isfile(fileName):

            font =ttLib.TTFont(fileName)
            name,family=__extractFontName(font)
            for key,value in abbDict.items():
                if key in name:
                    name=name.replace(key,value)
                if key.capitalize() in name:
                    name = name.replace(key.capitalize(), value)
            outputDict["fonts"][name.replace(" ","")]=os.path.split(fileName)[-1]

    with open(jsonPath,"w") as jsonOutputData:
        json.dump(outputDict,jsonOutputData)

if __name__ == "__main__":
    createJsonFile()