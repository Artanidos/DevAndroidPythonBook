# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.12.3)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xf5\
\x69\
\x6d\x70\x6f\x72\x74\x20\x51\x74\x51\x75\x69\x63\x6b\x20\x32\x2e\
\x30\x0a\x69\x6d\x70\x6f\x72\x74\x20\x51\x74\x51\x75\x69\x63\x6b\
\x2e\x43\x6f\x6e\x74\x72\x6f\x6c\x73\x20\x32\x2e\x35\x0a\x0a\x41\
\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x57\x69\x6e\x64\x6f\x77\
\x20\x7b\x0a\x20\x20\x20\x20\x76\x69\x73\x69\x62\x6c\x65\x3a\x20\
\x74\x72\x75\x65\x0a\x0a\x20\x20\x20\x20\x54\x65\x78\x74\x20\x7b\
\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x61\x6e\x63\x68\x6f\x72\x73\
\x2e\x68\x6f\x72\x69\x7a\x6f\x6e\x74\x61\x6c\x43\x65\x6e\x74\x65\
\x72\x3a\x20\x70\x61\x72\x65\x6e\x74\x2e\x68\x6f\x72\x69\x7a\x6f\
\x6e\x74\x61\x6c\x43\x65\x6e\x74\x65\x72\x0a\x20\x20\x20\x20\x20\
\x20\x20\x20\x61\x6e\x63\x68\x6f\x72\x73\x2e\x76\x65\x72\x74\x69\
\x63\x61\x6c\x43\x65\x6e\x74\x65\x72\x3a\x20\x70\x61\x72\x65\x6e\
\x74\x2e\x76\x65\x72\x74\x69\x63\x61\x6c\x43\x65\x6e\x74\x65\x72\
\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x74\x65\x78\x74\x3a\x20\x22\
\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x22\x0a\x20\x20\x20\
\x20\x7d\x0a\x7d\
"

qt_resource_name = b"\
\x00\x08\
\x0f\xca\x5b\xbc\
\x00\x76\
\x00\x69\x00\x65\x00\x77\x00\x2e\x00\x71\x00\x6d\x00\x6c\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x6b\xe0\xd3\x6b\x79\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()