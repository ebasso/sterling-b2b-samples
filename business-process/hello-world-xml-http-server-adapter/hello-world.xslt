<?xml version="1.0"?>
<xsl:transform exclude-result-prefixes="xsl" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="no"/>
    <xsl:template match="/">
    <book>
        <title><xsl:value-of select="/ResponseData/book/title"/>"</title>
        <author><xsl:value-of select="/ResponseData/book/author"/>"</author>
        <published>Year: <xsl:value-of select="/ResponseData/book/published"/>"</published>
    </book>
    </xsl:template>
</xsl:transform>