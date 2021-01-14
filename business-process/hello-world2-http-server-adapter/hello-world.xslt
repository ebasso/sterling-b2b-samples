<?xml version="1.0"?>
<xsl:transform exclude-result-prefixes="xsl" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" indent="yes"/>
    <xsl:template match="/">
    <HTML><BODY>
    <p>data="<xsl:value-of select="/ResponseData/data"/>"</p>
    <br/>

    <p>new page="<xsl:value-of select="/ResponseData/newpage"/>"</p>
    <br/>

    <p>noresult="<xsl:value-of select="/ResponseData/noresult"/>"</p>
    <br/>
    </BODY></HTML>
    </xsl:template>
</xsl:transform>