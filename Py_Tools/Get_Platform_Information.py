import platform as pltform
import os as OSCMD
import logging as logg

'''
 Objective: Get current program path
 Author   : Ronnie
 Date     : 10/04/2016
 Pyhton Libraty : platform

'''

class Get_Platform_Information(object):

    def __init__(self):
        print " Include PlatformInfo...."

    def getCurrntPlatform(self):
        return pltform.system()

    def getCurrentPath(self):
        logInfo = logg.INFO
        logg.basicConfig(format='%(levelname)s:%(message)s', level=logInfo)
        try:
            if self.getCurrntPlatform() == 'Windows': # For Window only
                OSCMD.chdir("..")
                currtPath = OSCMD.getcwd()
                return currtPath
            else:  # For other OS
                #TODO Linux need to define
                currtPath = OSCMD.getcwd()
                return currtPath
        except:
            logg.debug('-aPlatformLibrary ')


    def setToXML2Path(self):
        logInfo = logg.INFO
        logg.basicConfig(format='%(levelname)s:%(message)s', level=logInfo)
        try:
            if self.getCurrntPlatform() == 'Windows': # For Window only
                OSCMD.chdir("..")
                newPath = OSCMD.path.expanduser(OSCMD.getcwd()+'\\XMLnXML')
                OSCMD.chdir(newPath)
                currtPath = OSCMD.getcwd()
                return currtPath
            else:  # For other OS
                # TODO Linux need to define
                currtPath = OSCMD.getcwd()
                return currtPath
        except:
            logg.debug('-aPlatformLibrary ')
