<?xml version="1.0"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:urn="someurn">

<xsl:output method="text" />

<xsl:template match="/PullList">
    <xsl:for-each select="MessageName">
        <xsl:value-of select="text()"/>
        <xsl:text>&#10;</xsl:text>
    </xsl:for-each>
 </xsl:template>

</xsl:stylesheet>