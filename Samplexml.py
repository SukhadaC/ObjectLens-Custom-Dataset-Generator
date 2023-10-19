import  xml.etree.ElementTree as ET
import os

def CreateXML(xmin,ymin,xmax,ymax,xmlname,imagename_,shape):
 root=ET.Element("annotation")
 
 imagename=ET.Element("imagename")
 imagename.text=imagename_
 root.append(imagename)

 filename=ET.Element("filename")
 filename.text=xmlname
 root.append(filename)

 frame_size=ET.Element("frame_size")
 root.append(frame_size)
 width=ET.SubElement(frame_size,"width")
 width.text=shape[1]+shape[2]+shape[3]
 
 height=ET.SubElement(frame_size,"height")
 height.text=shape[5]+shape[6]+shape[7]+shape[8]
 channel=ET.SubElement(frame_size,"channel")
 channel.text=shape[11]

 object_=ET.Element("object")
 root.append(object_)
 name=ET.SubElement(object_,"name")
 name.text='BOH'


 
 
 
 dimensions=ET.SubElement(object_,"dimensions")

 Xmin=ET.SubElement(dimensions,"Xmin")
 Xmin.text=xmin
 Ymin=ET.SubElement(dimensions,"Ymin")
 Ymin.text=ymin

 Xmax=ET.SubElement(dimensions,"Xmax")
 Xmax.text=xmax
 Ymax=ET.SubElement(dimensions,"Ymax")
 Ymax.text=ymax

 tree=ET.ElementTree(root)
 sample=open(xmlname,'wb')
 tree.write(sample)

