#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf epson-inkjet-printer-201207w_%s%slsb3.2_amd64.deb" % (get.srcVERSION(), Suffix))
    shelltools.system("tar xvf data.tar.gz")

def install():

    #/usr/share/cups/model/gutenprint/5.2/Global/stp-escp2-l210.5.2.sim.ppd.gz
    pisitools.insinto("/", "opt")
    #shelltools.system("rm -rf /usr/share/cups/model/Epson/")
    #shelltools.system("mv -u opt/epson-inkjet-printer-201207w/ppds/* /usr/share/cups/model/")
    #shelltools.system("mv -u opt/epson-inkjet-printer-201207w/lib64/* /usr/lib64/")
    #shelltools.system("mv -u opt/epson-inkjet-printer-201207w/cups/* /usr/share/cups/")
