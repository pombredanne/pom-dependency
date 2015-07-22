# create-pom-xml

##### Create pom.xml dynamically using python

##### Usage:
create_pom_xml.py accepts the following values into the function create_pom_xml

1.Project Group ID - As String
2. Project Artifact ID  - As String
3. Project Version - As string
4. These values will serve purpose in creating project values in pom.xml
5. Same values will serve in creating jar file after sucessful build with pom.xml
6. g is maven group ID as a list even if passing a single item
7. a is maven artifact ID as a list even if passing a single item
8. v is maven group ID as a list even if passing a single item
9. g,a,v are maven coordinates

###### Trying out:
1. In python repr, type python test_create_pom.py.
2. A pom.xml is created with the maven coordinates passed by calling the function.
3. Compile a new list from sources to create pom.xml that meet your criteria
 
