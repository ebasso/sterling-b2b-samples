<?xml version="1.0"?>
<xsl:transform exclude-result-prefixes="xsl" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" indent="no" />
    <xsl:template match="/">
<html>
<head>
    <meta charset="UTF-8"></meta>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta>
    <title>Code List Editor</title>
    <style>
        * { box-sizing: border-box; }
        body { margin: 0; font-family: Arial, Helvetica, sans-serif; padding: 8px; }
        h2 { font-size: 18px; }
        .topnav { overflow: hidden; background-color: #e9e9e9; }
        .topnav h1{float:left;display:block;color:#000;text-align:center;padding:14px 16px;text-decoration:none;font-size:22px}
        .row{display:-ms-flexbox;display:block;-ms-flex-wrap:wrap;flex-wrap:wrap;margin:0 -16px}
        .col-25{-ms-flex:25%;flex:25%}
        .col-50{-ms-flex:50%;flex:50%}
        .col-75{-ms-flex:75%;flex:75%}
        .col-25,.col-50,.col-75{padding:0 16px}
        .container{padding:5px 25px 15px 20px;border:1px solid #d3d3d3;border-radius:3px}
        /* Style the form - display items horizontally */
        .form-inline{display:flex;flex-flow:row wrap;align-items:center;margin:5px 20px 5px 0}
        /* Add some margins for each label */
        .form-inline label{margin:5px 10px 5px 0}
        /* Style the input fields */
        .form-inline input{vertical-align:middle;margin:5px 10px 5px 0;padding:10px;border:1px solid #ddd}
        /* Style the submit button */
        .form-inline button{padding:10px 20px;background-color:#1e90ff;border:1px solid #ddd;color:#fff}
        .form-inline button:hover{background-color:#4169e1}

        .mybutton{padding:5px;background-color:#1e90ff;border:1px solid #ddd;color:#fff}

        .searchResultsTable {font-family:arial,sans-serif;border-collapse:collapse;width:100%}
        .searchResultsTable td,th{border:1px solid #ddd;text-align:left;padding:8px}
        .searchResultsTable tr:nth-child(even){background-color:#ddd}
        /* The Modal (background) */
        .modal{display:none;position:fixed;z-index:1;padding-top:100px;left:0;top:0;width:100%;height:100%;overflow:auto;background-color:#000;background-color:rgba(0,0,0,.4)}
        /* Modal Content */
        .modal-content{background-color:#fefefe;margin:auto;padding:20px;border:1px solid #888;width:80%}
        /* The Close Button */
        .close{float:right;font-size:28px;font-weight:700;padding:20px}
        .close:hover,.close:focus{color:#000;text-decoration:none;cursor:pointer}.close:hover,.close:focus{color:#000;text-decoration:none;cursor:pointer}
    </style>
    <script>
        function clearSearchForm() {
          document.getElementById('sLN').value = '';
          document.getElementById('sSIt').value = '';
          document.getElementById('sRIt').value = '';
          document.getElementById('searchResults').innerHTML = '';
        }

        function validateSearchForm() {
            var a = document.getElementById('sLN').value;
            var b = document.getElementById('sSIt').value;
            var c = document.getElementById('sRIt').value;

            if ( (a==="" || a==null) &amp;&amp; (b==="" || b==null)  &amp;&amp; (c==="" || c==null)){
                return false;
            }

            if (a==="" || a==null) {
                return false;
            }
        }

        function editForm(fLN,fSI,fRI,fLV,fSIt,fRIt,fDesc,fT1,fT2,fT3,fT4,fT5,fT6,fT7,fT8,fT9) {
            document.getElementById("myModal").style.display = "block";

            document.getElementById('mLN').value = fLN;
            document.getElementById('mSI').value = fSI;
            document.getElementById('mRI').value = fRI;
            document.getElementById('mSIt').value = fSIt;
            document.getElementById('mRIt').value = fRIt;
            document.getElementById('mDesc').value = fDesc;
            document.getElementById('mT1').value = fT1;
            document.getElementById('mT2').value = fT2;
            document.getElementById('mT3').value = fT3;

            document.getElementById('LN').value = fLN;
            document.getElementById('SI').value = fSI;
            document.getElementById('RI').value = fRI;
            document.getElementById('LV').value = fLV;
            document.getElementById('SIt').value = fSIt;
            document.getElementById('RIt').value = fRIt;
            document.getElementById('Desc').value = fDesc;
            document.getElementById('T1').value = fT1;
            document.getElementById('T2').value = fT2;
            document.getElementById('T3').value = fT3;
            document.getElementById('T4').value = fT4;
            document.getElementById('T5').value = fT5;
            document.getElementById('T6').value = fT6;
            document.getElementById('T7').value = fT7;
            document.getElementById('T8').value = fT8;
            document.getElementById('T9').value = fT9;
        }

        function closeForm() {
          document.getElementById("myModal").style.display = "none";
        }


        function validateCodeListEditorForm() {
            var nSI = document.getElementById('mSI').value; // New Value
            var oSI = document.getElementById('SI').value;  // Old Value
            var nRI = document.getElementById('mRI').value;
            var oRI = document.getElementById('RI').value;
            var nSIt = document.getElementById('mSIt').value;
            var oSIt = document.getElementById('SIt').value;
            var nRIt = document.getElementById('mRIt').value;
            var oRIt = document.getElementById('RIt').value;
            var nDesc = document.getElementById('mDesc').value;
            var oDesc = document.getElementById('Desc').value;
            var nT1 = document.getElementById('mT1').value;
            var oT1 = document.getElementById('T1').value;
            var nT2 = document.getElementById('mT2').value;
            var oT2 = document.getElementById('T2').value;
            var nT3 = document.getElementById('mT3').value;
            var oT3 = document.getElementById('T3').value;

            if ( (nSI === oSI) &amp;&amp; (nRI === oRI) &amp;&amp; (nSIt === oSIt) &amp;&amp; (nRIt === oRIt) &amp;&amp;
                 (nDesc === oDesc) &amp;&amp; (nT1 === oT1) &amp;&amp; (nT2 === oT2) &amp;&amp; (nT3 === oT3)){
                return false;
            }
            return true;
        }
    </script>
</head>

<body>
    <div class="topnav">
        <h1>Code List Editor</h1>
    </div>
    <div id="searchFields">
        <h2> Search for:</h2>
        <div class="row">
            <div class="col-75">
                <div class="container">
                    <form class="form-inline" action="/codelisteditor" onsubmit="return validateSearchForm()">
                      <table>
                        <tr>
                          <td>
                            <label for="sLN">* List Name:</label>
                            <input type="text" id="sLN" placeholder="Enter List Name" name="sLN" />
                          </td>
                        </tr>
                        <tr>
                          <td>
                          <label for="sSIt">Sender Item:</label>
                          <input type="text" id="sSIt" placeholder="Enter Sender Item" name="sSIt" />
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <label for="sRIt">Receiver Item:</label>
                            <input type="text" id="sRIt" placeholder="Enter Receiver Item" name="sRIt" />
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <button type="button" onclick="clearSearchForm()">Clear Form and Fields</button> &#160;&#160;&#160;
                            <button type="submit">Submit</button>
                          </td>
                        </tr>
                    </table>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <div id="searchResults">
        <xsl:if test="/ResponseData/newpage">
            <!-- Nothing to do -->
        </xsl:if>
        <xsl:if test="/ResponseData/result">
            <h2><xsl:value-of select="/ResponseData/result" /></h2>
        </xsl:if>
        <xsl:if test="/ResponseData/data">
            <h2>Results:</h2>
            <div class="row">
                <div class="col-75">
                    <div class="container">
                        <table class="searchResultsTable">
                            <tr>
                              <th>Sender Item</th>
                              <th>Receiver Item</th>
                              <th>Description</th>
                              <th></th>
                            </tr>
                            <xsl:for-each select="/ResponseData/data/Row1">
                                <tr>
                                    <td><xsl:value-of select="SENDER_ITEM" /></td>
                                    <td><xsl:value-of select="RECEIVER_ITEM" /></td>
                                    <td><xsl:value-of select="DESCRIPTION" /></td>
                                    <td><button class="mybutton"><xsl:attribute name="onClick">editForm('<xsl:value-of select="LIST_NAME" />','<xsl:value-of select="SENDER_ID" />','<xsl:value-of select="RECEIVER_ID" />','<xsl:value-of select="LIST_VERSION" />','<xsl:value-of select="SENDER_ITEM" />','<xsl:value-of select="RECEIVER_ITEM" />','<xsl:value-of select="DESCRIPTION" />','<xsl:value-of select="TEXT1" />','<xsl:value-of select="TEXT2" />','<xsl:value-of select="TEXT3" />','<xsl:value-of select="TEXT4" />','<xsl:value-of select="TEXT5" />','<xsl:value-of select="TEXT6" />','<xsl:value-of select="TEXT7" />','<xsl:value-of select="TEXT8" />','<xsl:value-of select="TEXT9" />')</xsl:attribute>Edit</button></td>
                                </tr>
                            </xsl:for-each>

                        </table>
                    </div>
                </div>
            </div>
        </xsl:if>
    </div>
    <div id="myModal" class="modal">

      <!-- Modal content -->
      <div class="modal-content">
        <div class="topnav">
            <h1>Code List Editor</h1>
            <span class="close">&#215;</span>
        </div>

        <form class="form-inline" action="/codelisteditor" method="post" onsubmit="return validateCodeListEditorForm()">
          <input type="hidden" id="LN"  name="LN" value="" />
          <input type="hidden" id="SI"  name="SI" value="" />
          <input type="hidden" id="RI"  name="RI" value="" />
          <input type="hidden" id="LV"  name="LV" value="" />
          <input type="hidden" id="SIt" name="SIt" value=""/>
          <input type="hidden" id="RIt" name="RIt" value=""/>
          <input type="hidden" id="Desc" name="Desc" value="" />
          <input type="hidden" id="T1"  name="T1" value="" />
          <input type="hidden" id="T2"  name="T2" value="" />
          <input type="hidden" id="T3"  name="T3" value="" />
          <input type="hidden" id="T4"  name="T4" value="" />
          <input type="hidden" id="T5"  name="T5" value="" />
          <input type="hidden" id="T6"  name="T6" value="" />
          <input type="hidden" id="T7"  name="T7" value="" />
          <input type="hidden" id="T8"  name="T8" value="" />
          <input type="hidden" id="T9"  name="T9" value="" />

          <table>
            <tr>
              <td>
                <label for="mLN">List Name:</label>
                <input type="text" id="mLN" name="mLN" value="" disabled="" />
              </td>
              </tr>
              <tr>
              <td>
                <label for="mSI">Sender Id:</label>
                <input type="text" id="mSI" name="mSI" value="" disabled="" />
                <label for="mRI">Receiver Id:</label>
                <input type="text" id="mRI" name="mRI" value="" disabled=""/>
              </td>
              </tr>
              <tr>
              <td>
                <label for="mSIt">Sender Item:</label>
                <input type="text" id="mSIt" name="mSIt" value="" />
              </td>
              </tr>
              <tr>
              <td>
                <label for="mRIt">Receiver Item:</label>
                <input type="text" id="mRIt" name="mRIt" value="" />
              </td>
            </tr>
              <tr>
              <td>
                <label for="mDesc">Description:</label>
                <input type="text" id="mDesc" name="mDesc" value="" />
              </td>
              </tr>
              <tr>
              <td>
                <label for="mT1">Text1:</label>
                <input type="text" id="mT1" name="mT1" value="" />
              </td>
              </tr>
              <tr>
              <td>
                <label for="mT2">Text2:</label>
                <input type="text" id="mT2" name="mT2" value="" />
              </td>
              </tr>
              <tr>
              <td>
                <label for="mT3">Text3:</label>
                <input type="text" id="mT3" name="mT3" value="" />
              </td>
              </tr>
              <tr>
              <td>
                <button type="submit">Submit</button>
              </td>
            </tr>
        </table>
        </form>
      </div>

    </div>
  <script>
    var modal = document.getElementById("myModal");
    var btn = document.getElementById("myBtn");
    var span = document.getElementsByClassName("close")[0];

    span.onclick = function() {
      modal.style.display = "none";
    }

    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
</script>
</body>

</html>
    </xsl:template>
</xsl:transform>
