from lxml import etree
from time import gmtime, strftime

'''
 Objective: Transform using XSLT to XML
 Author   : Ronnie
 Date     : 10/04/2016
 Pyhton Libraty : XML.etree


'''
class TransformationFileXSLT_From_XML_Data(object):
    def __init__(self):
        print " Include XSLT Transformation...."

    def writeResult(self, txtString,targetSourceLocation):
        # print '\n' + txtString
        with open(targetSourceLocation, "ab") as text_file:
            text_file.write(txtString)
        return txtString

    def XSLTTransformation(self,currentPath,XSLTFile, XMLDataUsedFile,targetSourceLocation,componentType,productID):

        stext = componentType

        xsltTemplate = currentPath+"\\XSLT\\"+XSLTFile
        xslt_pmf_POC = etree.parse(xsltTemplate)

        print "XSLT path: %s" %(xsltTemplate)

        transform = etree.XSLT(xslt_pmf_POC)

        XMLDataLocation = currentPath+"\\XmlData\\"+XMLDataUsedFile

        print "XML data location: %s" %(XMLDataLocation)

        with open(XMLDataLocation, "r") as f:
        ###f = open(XMLDataLocation, 'r')
            doc = etree.parse(f)

        if componentType.upper() == 'LOB_A':

            plain_string_value = etree.XSLT.strparam(
                                """LOB1""")

            # Dont delete
            # result_tree = transform(doc,ossName=etree.XPath("/a/b[3]/text()"),msgID=etree.XPath("/a/b[2]/text()"))
            result_tree = transform(doc, ossName=plain_string_value, **{'msgID': '99097'})
            # print result_tree
            pintme = self.writeResult(result_tree,targetSourceLocation)

        elif componentType.upper() == 'LOB_B':

            strDatetime = strftime("%d/%m/%Y %H:%M:%S", gmtime())

            plain_string_value = etree.XSLT.strparam("""LOB_Title""")
            e2eData_string_value = etree.XSLT.strparam("""E2E""")
            stateCode_string_value = etree.XSLT.strparam("""OK""")
            fromServiceAddress_string_value = etree.XSLT.strparam("""to""")
            addressReplyTo_string_value = etree.XSLT.strparam("""from""")
            addreesFaultTo_string_value = etree.XSLT.strparam("""from""")
            action_string_value = etree.XSLT.strparam("""Capability""")
            id_string_value = etree.XSLT.strparam("""to""")
            dateTime_string_value = etree.XSLT.strparam(str(strDatetime))
            productId_string_value = etree.XSLT.strparam(productID)
            internalName_string_value = etree.XSLT.strparam("""""")

            result_tree = transform(doc, ossName=plain_string_value,
                                    e2eData=e2eData_string_value,
                                    stateCode=stateCode_string_value,
                                    fromServiceAddress=fromServiceAddress_string_value,
                                    addressReplyTo=addressReplyTo_string_value,
                                    addreesFaultTo=addreesFaultTo_string_value,
                                    action=action_string_value,
                                    id=id_string_value,
                                    dateTimeMY=dateTime_string_value,
                                    productId=productId_string_value,
                                    internalName=internalName_string_value,
                                    **{'msgID': '99097'})
            pintme = self.writeResult(result_tree, targetSourceLocation)
        else:
            print "XSLT Transformation for other component is currently empty"
