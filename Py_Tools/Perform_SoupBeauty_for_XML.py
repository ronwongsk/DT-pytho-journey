from bs4 import BeautifulSoup,NavigableString
from lxml import etree, objectify
from lxml.etree import tostring
import string as replacementStr



'''
 Objective: Perform and clean up XML , using Beautishop
 Author   : Ronnie
 Date     : 10/04/2016
 Pyhton Libraty : XML.etree

'''

class Perform_SoupBeauty_for_XML(object):

    def __init__(self):
        print " Include Soup Beauty Object ...."

    def getNonDupl_partNumber(self,soupObj):
        neededList = []
        countAKG = len(soupObj)
        #print soupObj
        for i in range(1, countAKG):
            if soupObj[i] <> "\n":
                # print soup.a.b.c.d.contents[i]
                try:
                    try:
                        neededList.append(soupObj[i].itemname.string)
                    except:
                        #neededList.append(soupObj[i].itemnumber.string)
                        try:
                            neededList.append(soupObj[i].partnumber.string)
                        except:
                            #neededList.append(soupObj[i].partnumber.string)
                            raise
                except Exception as e:
                    print "Error %s" %(e.message)
                neededListNew= list(set(neededList))
        return neededListNew


    def getList_SoupObj(self,soupObj, tmpStr):
        neededList = []
        countAKG = len(soupObj)
        for i in range(1,countAKG):
            if soupObj[i] <> "\n":
            #print soup.a.b.c.d.contents[i]
              try:
                try:
                    if (soupObj[i].partnumber.string == tmpStr):
                        neededList.append(soupObj[i])
                    else:
                        neededList.append(soupObj[i])
                except:
                    try:
                        if (soupObj[i].itemname.string == tmpStr):
                            neededList.append(soupObj[i])
                        else:
                            neededList.append(soupObj[i])
                    except:
                            raise
              except Exception as e:
                print "Error %s" %(e.message)

        return neededList

    def getList_SoupObjNoDupl(self, soupObj, tmpStr,accessStr):
        neededList = []
        countAKG = len(soupObj)
        neededListNew = []
        try:
            try:
                for i in range(1, countAKG):
                    if soupObj[i] <> "\n":
                        #print soup.a.b.c.d.contents[i]
                        if (soupObj[i].partnumber.string == tmpStr):
                            neededList.append(soupObj[i])
                            neededListNew = list(set(neededList))
            except:
                try:
                    myReturn = ""
                    for child in soupObj:
                        if (isinstance(child, NavigableString) == False):
                            if child.partNumber.string == tmpStr:
                                asll = ''.join(str(e) for e in child.contents)
                                if accessStr == 'e':
                                    new_str = replacementStr.replace("<AttributeName>HereStr</AttributeName>", "HereStr", asll)
                                    myReturn = myReturn.__add__(new_str)
                                elif accessStr == 'a':
                                    myReturn = myReturn.__add__(asll)
                                    break
                                elif accessStr == 'd':
                                    new_str = replacementStr.replace("<AttributeDefinition>HereStr</AttributeDefinition>", "HereStr", asll)
                                    myReturn = myReturn.__add__(new_str)
                    neededListNew = myReturn
                except:
                    try:
                        for i in range(1, countAKG):
                            if soupObj[i] <> "\n":
                                # print soup.a.b.c.d.contents[i]
                                if (soupObj[i].itemname.string == tmpStr):
                                    neededList.append(soupObj[i])
                                    neededListNew = list(set(neededList))
                    except:
                        myReturn = ""
                        for child in soupObj:
                            if (isinstance(child, NavigableString) == False):
                                if child.ItemName.string == tmpStr:
                                    asll = ''.join(str(e) for e in child.contents)
                                    if accessStr == 'e':
                                        new_str = replacementStr.replace("<APL>HereStr</APL>",
                                                                         "HereStr", asll)
                                        myReturn = myReturn.__add__(new_str)
                                    elif accessStr == 'a':
                                        myReturn = myReturn.__add__(asll)
                                        break
                                    elif accessStr == 'd':
                                        new_str = replacementStr.replace(
                                            "<ParentProductID>HereStr</ParentProductID>", "HereStr", asll)
                                        myReturn = myReturn.__add__(new_str)
                                        break
                                    elif accessStr == 'f':
                                        new_str = replacementStr.replace(
                                            "<Parametric>HereStr</Parametric>", "HereStr", asll)
                                        myReturn = myReturn.__add__(new_str)
                                    elif accessStr == 'g':
                                        new_str = replacementStr.replace(
                                            "<AttributeDefinition>HereStr</AttributeDefinition>", "HereStr", asll)
                                        myReturn = myReturn.__add__(new_str)
                                    elif accessStr == 'h':
                                        new_str = replacementStr.replace(
                                            "<Tax_Rule>HereStr</Tax_Rule>", "HereStr", asll)
                                        myReturn = myReturn.__add__(new_str)
                                    elif accessStr == 'i':
                                        new_str = replacementStr.replace(
                                            "<TariffRating>HereStr</TariffRating>", "HereStr", asll)
                                        myReturn = myReturn.__add__(new_str)
                                elif child.ItemName.string == tmpStr:
                                    if accessStr == 'h':
                                        new_str = replacementStr.replace(
                                            "<Tax_Rule>HereStr</Tax_Rule>", "HereStr", asll)
                                        myReturn = myReturn.__add__(new_str)

                        neededListNew = myReturn

        except Exception as e:
            print "Error %s - %s" % (e.message,e.args)
        # -------------------------------------------------------------------------------
        return neededListNew

    def getParseToBeatifulSoup(self,fInput):
        doc = etree.parse(fInput)
        # docType01 = fromstring(doc)
        doc = tostring(doc, pretty_print=True).strip()
        soup = BeautifulSoup(doc, "lxml")
        return soup

    def getBasicBeatifulSoup(self, fInput):
        soup = BeautifulSoup(fInput, "xml")
        return soup

    def getCustomXMLAtrributeBaseSoupDotCommand(self,inOBj,aList):
        myReturn=""
        for ixp in aList:
            #print ((inOBj)(ixp)[0])
            print inOBj
            myReturn= myReturn.__add__(str(inOBj(ixp)[0]))
        return myReturn

    def getCustomXMLAtrributeWithList(self, aList):
        myReturn = ""
        for ixp in aList:
            # print ((inOBj)(ixp)[0])
            myReturn = myReturn.__add__(str(ixp))
        return myReturn

    # Passing Mapped-XML and inject into Data XML using XML C Template which in the memory
    def quickReplaceMEMxml_template(self,soupObj,xml_template,replacementSection):
        aStr=""
        a = self.getList_SoupObj(soupObj,"")
        for ix in range (0,len(a)-1):
            if ix == 0:
                aStr = str(a[ix])
            else:
                aStr = aStr.__add__(str(a[ix]))

        new_str= replacementStr.replace(xml_template,replacementSection,aStr)
        return new_str

    # Direct Passing Mapped-XML and inject into Data XML using XML C Template which in the memory
    def directReplaceMEMxml_template(self,aStr,xml_template,replacementSection):
        new_str= replacementStr.replace(xml_template,replacementSection,aStr)
        return new_str

    # Create XML and replace XML function
    def writeResult(self,fileName,txtString):
         # print '\n' + txtString
        with open(fileName, "ab") as text_file:
            text_file.write('\n' + txtString)
        return True

    # Read XML Template to memory
    def readXMLModule(self,thePath,fileName):
        with open(thePath+fileName, 'r') as fileReadFie:
            txtdata = fileReadFie.read()
            #data = myfile.read().replace('\n', '')
        return txtdata
