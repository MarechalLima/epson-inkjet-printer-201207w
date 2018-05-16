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

    pisitools.insinto("/", "opt") 
    pisitools.dosym("/opt/epson-inkjet-printer-201207w/ppds/Epson", "/usr/share/ppd/Epson")
    pisitools.dosym("/opt/epson-inkjet-printer-201207w/lib64/libEpson_201207w.so.1.0.0", "/usr/lib64/libEpson_201207w.so.1.0.0")
    pisitools.dosym("/opt/epson-inkjet-printer-201207w/lib64/libEpson_201207w.MT.so.1.0.0", "/usr/lib64/libEpson_201207w.MT.so.1.0.0")
    pisitools.dosym("/opt/epson-inkjet-printer-201207w/cups/lib/filter/epson_inkjet_printer_filter", "/usr/lib/cups/filter/epson_inkjet_printer_filter")
