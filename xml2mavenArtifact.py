'''
Author: Sai Uday Shankar
'''

# This is a very specific  XML Parser.
# This parser requires any XML file to look like a maven pom.xml
# For looking at a sample look at the below URL
## https://maven.apache.org/guides/introduction/introduction-to-the-pom.html

import xmltodict
import re, sys

def xmlmvnparser(xmlfile):
    xmldoc = open(xmlfile, 'r')
    xmlcont = xmldoc.read()
    xmldoc.close()
    tree = xmltodict.parse(xmlcont)
    
    g_id = tree['project']['groupId']
    a_id = tree['project']['artifactId']
    ver = tree['project']['version']
    g = []
    a = []
    v = []
    dependencies = tree['project']['dependencies']
    mav_coords = []
    for item in dependencies['dependency']:

        g.append(str(item['groupId']))
        a.append(str(item['artifactId']))

        v.append(str(item['version']))
	
    return(g_id, a_id, ver, g, a, v)


if __name__ =='__main__':
    xmlparser('pom.xml')
    
