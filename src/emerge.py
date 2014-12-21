#!/usr/bin/env python

from time import sleep
import re


FILE="/var/log/emerge.log"

class emerge:
    """
    Class to read emerge.log / and watch for new events
    """
    def __init__(self):
        """
        Open emerge.log, readall, and watch for new line
        """
        self.file=open(FILE)
        self.lastline=None
        self.buff=self.readall()
        self.tot=0
        self.cur=0
        self.pkg=None

        for v in self.buff:
            self.parsing(v)


    def parsing(self,line):
        """
        Parse line and fill variables:
         - current package
         - current total action
         - current progress
        """
        m=re.search("emerge \(([0-9]*) of ([0-9]*)\) (.*) to",line)
        if (m):
            self.tot=int(m.group(2))
            self.cur=int(m.group(1))
            self.pkg=m.group(3)

        m=re.search("=== \(.*\) (.*) \(",line)
        if (m):
            self.action=m.group(1)

        m=re.search("\*\*\* (.*)",line)
        if (m):
            self.status=m.group(1)

    def dump(self):
        """
        Print variables
        """
        print ("%d of %d > %s %s (%s)"%(self.cur,self.tot,self.pkg,self.action,self.status))
        

    def readall(self):
        """
        Read all log file (init)
        """
        return self.file.readlines();

    def read(self):
        """
        Read line & launch parsing
        """
        self.lastline=self.file.readline()
        if (len(self.lastline)):
            self.parsing(self.lastline)
        return len(self.lastline)

    def __del__(self):
        """
        Close file emerge.log
        """
        self.file.close()


if (__name__== "__main__"):
    dd=emerge()
    dd.dump()
    while True:
        if (dd.read()):
            dd.dump()
        sleep(1)
