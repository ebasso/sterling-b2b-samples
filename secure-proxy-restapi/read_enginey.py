import requests
import json
import re
import xml.dom.minidom
import xml.etree.ElementTree as ET

# Set variables
ssp_cm_url = "<ssp_cm_url>"
ssp_admin_user = "<ssp_admin_user>"
ssp_admin_password = "<ssp_admin_password>"

def get_session_token():
    """
    Authenticate with the SSP and return a session token.
    """
    session_url = f"https://{ssp_cm_url}/sspcmrest/sspcm/rest/session"
    session_headers = {
        "Content-Type": "application/json"
    }
    session_data = {
        "userId": ssp_admin_user,
        "password": ssp_admin_password
    }

    session_response = requests.post(session_url, headers=session_headers, data=json.dumps(session_data), verify=False)

    if session_response.status_code == 200:
        # Extract session token using regex
        match = re.search(r'"sessionToken":"([a-zA-Z0-9+/=]+)"', session_response.text)
        if match:
            session_token = match.group(1)
            return session_token
        else:
            raise Exception("Session token not found in the response")
    else:
        raise Exception(f"Failed to get session token: {session_response.text}")

def prettify_xml(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def get_all_engine(session_token):
    """
    Create an engine on the SSP using the provided session token.
    """
    engine_url = f"https://{ssp_cm_url}/sspcmrest/sspcm/rest/engine/getAllEngines"
    engine_headers = {
        "X-Authentication": session_token,
        "Content-Type": "application/xml"
    }

    rsp = requests.get(engine_url, headers=engine_headers, verify=False)

    # Parse the XML data into a DOM object
    dom = xml.dom.minidom.parseString(rsp.text)

    # Pretty-print the XML
    pretty_xml_as_string = dom.toprettyxml()

    print('----------------------------------------------------')
    print(pretty_xml_as_string)
    print('----------------------------------------------------')

def get_engine(session_token, engineName):
    """
    Create an engine on the SSP using the provided session token.
    """
    engine_url = f"https://{ssp_cm_url}/sspcmrest/sspcm/rest/engine/getEngine/{engineName}"
    engine_headers = {
        "X-Authentication": session_token,
        "Content-Type": "application/xml"
    }

    rsp = requests.get(engine_url, headers=engine_headers, verify=False)

    # Parse the original XML string
    root = ET.fromstring(rsp.text)

    # Find the <value> tag and extract its text content
    value_content = root.find('.//value').text

    # Unescape the XML content in the <value> tag
    unescaped_value_content = value_content.replace('&lt;', '<').replace('&gt;', '>')

    print('----------------------------------------------------')
    print(unescaped_value_content)
    print('----------------------------------------------------')


# Main logic
if __name__ == "__main__":

    try:
        # Get session token
        session_token = get_session_token()
        print(f"Session Token: {session_token}")

        # getAllEngines
        get_all_engine(session_token)

        get_engine(session_token, 'ssp-engine')


    except Exception as e:
        print(e)
