<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:urn="someurn">
<xsl:output method="text" />
<xsl:template match="/This/PullList">/* Process Index Copy */
PIDXCPY PROCESS
   SNODE=<xsl:text>&#38;</xsl:text>node
   SNODEID=(<xsl:text>&#38;</xsl:text>user,<xsl:text>&#38;</xsl:text>pw)
<xsl:for-each select="MessageName">
CPY<xsl:value-of select="position()" /> COPY
     FROM (
         FILE="/mailbox/Inbox/<xsl:value-of select="text()"/>"
         SNODE
     )
     TO (
         FILE="<xsl:text>&#38;</xsl:text>path<xsl:value-of select="/This/SlashType" /><xsl:value-of select="text()" />"
         DISP=RPL
         PNODE
     )

IFCPY<xsl:value-of select="position()" /> IF (CPY<xsl:value-of select="position()" /> EQ 0) THEN
            RUN TASK SNODE
               PGM=MAILBOX_DELETE_FILE_RUNTASK
               SYSOPTS="filename=<xsl:value-of select="text()"/>;"
        EIF
</xsl:for-each>
PEND
</xsl:template>
</xsl:stylesheet>