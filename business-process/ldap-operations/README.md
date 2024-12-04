# LDAP Query


# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| demo-ldap-adapter.bpml          | Business Process that do LDAP Query |
| list-users.xml           | XSLT file to generate html output |
| list-groups.xml         | Business Process that do RestAPI Get |


# Steps to Run:


**On B2Bi Dashboard**


1) Login o Sterling B2B Console

2) Create a new LDAP Adapter: **LDAPAdapter**

```
Service Type:            LDAP Adapter
Description:             Generic LDAP Adapter 
Group Name:              None
```
and provide LDAP information:

```
LDAP Host: 
LDAP Port: 
Bind user: 
Bind user Password: 
```

3) Create a new Business Process: **Demo_LDAPAdapter**, using file **demo-ldap-adapter.bpml** 

4) Run the BP and provide file **list-users.xml** 

Check information on Process Dataa
