import xmltodict  # pip install xmltodict
import re
import string as str
import random as ran
from deepdiff import DeepDiff
from pprint import pprint
from lxml import etree
from xml.etree import ElementTree
from os import listdir
from os.path import isfile, join
import collections as COLlection


'''
 Objective: Perfrom different operation
 Author   : Ronnie
 Date     : 10/04/2016
 Pyhton :Lib : deepdif, XMLtodict, XML.etree
'''

class XMLs_Deep_Diff_Function(object):
    def __init__(self, xml1, xml2):
        self.dict1 = xml1
        self.dict2 = xml2

    def diff(list1, list2):
        c = set(list1).union(set(list2))
        d = set(list1).intersection(set(list2))
        return list(c - d)

    def normalise_dict(self, d):
        """
        Recursively convert dict-like object (eg OrderedDict) into plain dict.
        Sorts list values.
        """
        out = {}
        for k, v in dict(d).iteritems():
            if hasattr(v, 'iteritems'):
                out[k] = self.normalise_dict(v)
            elif isinstance(v, list):
                out[k] = []
                for item in sorted(v):
                    if hasattr(item, 'iteritems'):
                        out[k].append(self.normalise_dict(item))
                    else:
                        out[k].append(item)
            else:
                out[k] = v
        return out

    def deepDiffXML(self,a, b):
        """
        Compares two XML documents (as string or etree)

        Does not care about element order
        """
        if not isinstance(a, basestring):
            a = etree.tostring(a)
        # print  a
        if not isinstance(b, basestring):
            b = etree.tostring(b)

        a = xmltodict.parse(a)
        b = xmltodict.parse(b)
        #c = pprint(DeepDiff(a, b,ignore_order=True),indent=2, width=50)
        c = DeepDiff(a, b,ignore_order=True)
        #pprint(DeepDiff(a, b,ignore_order=True),indent=2, width=50)
        d = a==b
        #result = c
        #print len(c)
        return c

    def xml_compare(self, a, b):
        """
        Compares two XML documents (as string or etree)

        Does not care about element order
        """
        if not isinstance(a, basestring):
            a = etree.tostring(a)
        # print  a
        if not isinstance(b, basestring):
            b = etree.tostring(b)

        a = xmltodict.parse(a)
        #print a
        ab = COLlection.OrderedDict(sorted(a.items(),key=lambda t:t[0]))
        #print ab
        b = xmltodict.parse(b)
        ba = COLlection.OrderedDict(sorted(b.items(), key=lambda t: t[0]))
        #print ba
        c = DeepDiff(ab, ba,ignore_order=True)

        if len(c) == 0:
            return True

        if len(c) > 0:
            return False



    def excluded_eTree_elements(self,root_Master,list_To_exclude):
        print "Implement Filter List . . . ."
        if len(list_To_exclude) <> 0:
            iterLists = iter(list_To_exclude)
            for iterList in iterLists:
                for rootIter in root_Master.findall(iterList):
                    # NOTE:  for rootIter in root_Master.iter(iterList): --> Filter.this=messageId,address
                    # NOTE:  for rootIter in root_Master.findall(iterList):  ->Filter.this=.//serviceAddressing/messageId,.//serviceAddressing/to/address
                    # set XML to empty
                    rootIter.text = ""
        else:
            print " Filter list <<None>> "


    def getTheXMLtoString(self, inPath,exceluding_list):
        tree = ElementTree.parse(inPath)
        root = tree.getroot()

        # Perform Exclude item from XML
        if len(exceluding_list) > 2:
            self.excluded_eTree_elements(root,exceluding_list)

        xml1 = ElementTree.tostring(root)

        return xml1

    def listFolderFile(self, mypath):
        return [f for f in listdir(mypath) if isfile(join(mypath, f))]

    def listFileExist(self, targetPath, fileNAme):
        return isfile(join(targetPath, fileNAme))

    def countFolderFiles(self, mypath):
            try:
                return len(listdir(mypath))
            except:
               return 0

    def listPerfromRegularExpressionWithDefinedCode(self,lines,regularEXp):
        #r'^[SsPpEe][Ii0-9]\d{5,}'
        for line in lines:
            searchObj = re.search( regularEXp, line, re.M|re.I)
            if searchObj:
                return searchObj.group()
            else:
                return "XFOUND." + self.id_generator()

    def id_generator(self,size=6, chars=str.ascii_uppercase + str.digits):
        return ''.join(ran.choice(chars) for _ in range(size))



