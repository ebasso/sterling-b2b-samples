<?xml version="1.0"?>
<xsl:transform exclude-result-prefixes="xsl" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" indent="yes" />
    <xsl:template match="/">
        <html>

        <head>
            <meta charset="UTF-8">
            </meta>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </meta>
            <title>Sterling File Gateway - Search Page</title>
            <style>
                * {
                    box-sizing: border-box;
                }

                body {
                    margin: 0;
                    font-family: Arial, Helvetica, sans-serif;
                    padding: 8px;
                }

                h2 {
                    font-size: 18px;
                }

                .topnav {
                    overflow: hidden;
                    background-color: #e9e9e9;
                }

                .topnav h1 {
                    float: left;
                    display: block;
                    color: black;
                    text-align: center;
                    padding: 14px 16px;
                    text-decoration: none;
                    font-size: 22px;
                }

                .row {
                    display: -ms-flexbox;
                    /* IE10 */
                    display: block;
                    -ms-flex-wrap: wrap;
                    /* IE10 */
                    flex-wrap: wrap;
                    margin: 0 -16px;
                }

                .col-75 {
                    -ms-flex: 75%;
                    /* IE10 */
                    flex: 75%;
                    padding: 0 16px;
                }

                .container {
                    padding: 5px 25px 15px 20px;
                    border: 1px solid lightgrey;
                    border-radius: 3px;
                }

                /* Style the form - display items horizontally */
                .form-inline {
                    display: flex;
                    flex-flow: row wrap;
                    align-items: center;
                    margin: 5px 20px 5px 0;
                }

                /* Add some margins for each label */
                .form-inline label {
                    margin: 5px 10px 5px 0;
                }

                /* Style the input fields */
                .form-inline input {
                    vertical-align: middle;
                    margin: 5px 10px 5px 0;
                    padding: 10px;
                    border: 1px solid #ddd;
                }

                /* Style the submit button */
                .form-inline button {
                    padding: 10px 20px;
                    background-color: dodgerblue;
                    border: 1px solid #ddd;
                    color: white;
                }

                .form-inline button:hover {
                    background-color: royalblue;
                }

                table {
                    font-family: arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                }

                td,
                th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }

                tr:nth-child(even) {
                    background-color: #dddddd;
                }
            </style>
            <script>
                function clearForm() {
                    document.getElementById('partnerName').value = '';
                    document.getElementById('partnerCode').value = '';
                    document.getElementById('loginId').value = '';
                    document.getElementById('firstName').value = '';
                    document.getElementById('lastName').value = '';
                    document.getElementById('lastName').value = '';
                    document.getElementById('searchResults').innerHTML = '';
                }

                function validateFormPartnerName() {
                    var a = document.getElementById('partnerName').value;
                    if (a==="" || a==null) {
                        return false;
                    }
                }

                function validateFormPartnerCode() {
                    var a = document.getElementById('partnerCode').value;
                    if (a==="" || a==null) {
                        return false;
                    }
                }

                function validateFormLoginID() {
                    var a = document.getElementById('loginId').value;
                    if (a==="" || a==null) {
                        return false;
                    }
                }

                function validateFormFirstNameLastName() {
                    var a = document.getElementById('firstName').value;
                    var b = document.getElementById('lastName').value;
                    if ( (a==="" || a==null) &amp;&amp; (b==="" || b==null)){
                        return false;
                    }
                }
            </script>
        </head>

        <body>
            <div class="topnav">
                <h1>Advanced Search for Sterling File Gateway Partners</h1>
            </div>
            <div id="searchFields">
                <h2> Search for:</h2>
                <div class="row">
                    <div class="col-75">
                        <div class="container">
                            <form class="form-inline" action="/search" onsubmit="return validateFormPartnerName()">
                                <label for="partnerName">Partner Name:</label>
                                <input type="text" id="partnerName" placeholder="Enter Partner Name" name="partnerName"></input>
                                <button type="submit">Submit</button>
                            </form>
                            <form class="form-inline" action="/search" onsubmit="return validateFormPartnerCode()">
                                <label for="partnerCode">Parner Code:</label>
                                <input type="text" id="partnerCode" placeholder="Enter Partner Code" name="partnerCode"></input>
                                <button type="submit">Submit</button>
                            </form>
                            <form class="form-inline" action="/search" onsubmit="return validateFormLoginID()">
                                <label for="loginId">Login ID:</label>
                                <input type="text" id="loginId" placeholder="Enter Login ID" name="loginId"></input>
                                <button type="submit">Submit</button>
                            </form>
                            <form class="form-inline" action="/search" onsubmit="return validateFormFirstNameLastName()">
                                <label for="firstName">First Name:</label>
                                <input type="text" id="firstName" placeholder="Enter First Name" name="firstName"></input>
                                <label for="lastName">Last Name:</label>
                                <input type="text" id="lastName" placeholder="Enter Last Name" name="lastName"></input>
                                <button type="submit">Submit</button>
                            </form>
                            <form class="form-inline" >
                                <button type="button" onclick="clearForm()">Clear Form and Fields</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>

            <div id="searchResults">
                <xsl:if test="/ResponseData/newpage">
                    <!-- Nothing to do -->
                </xsl:if>
                <xsl:if test="/ResponseData/noresult">
                    <h2>Query return 0 results!</h2>
                </xsl:if>
                <xsl:if test="/ResponseData/data">
                    <h2>Results:</h2>
                    <div class="row">
                        <div class="col-75">
                            <div class="container">
                                <table>
                                    <tr>
                                        <th>Partner Name</th>
                                        <th>Partner Code</th>
                                        <th>Login ID</th>
                                        <th>First Name</th>
                                        <th>Last Name</th>
                                    </tr>
                                    
                                    <xsl:for-each select="/ResponseData/data/Row1">
                                        <tr>
                                            <td><xsl:value-of select="ORGANIZATION_NAME" /></td>
                                            <td><xsl:value-of select="OKEY" /></td>
                                            <td><xsl:value-of select="LOGIN" /></td>
                                            <td><xsl:value-of select="FIRST_NAME" /></td>
                                            <td><xsl:value-of select="LAST_NAME" /></td>
                                        </tr>
                                    </xsl:for-each>
                                    
                                </table>
                            </div>
                        </div>
                    </div>
                </xsl:if>
            </div>
        </body>

        </html>
    </xsl:template>
</xsl:transform>