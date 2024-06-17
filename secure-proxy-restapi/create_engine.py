import requests
import json
import re

def get_session_token(ssp_cm_url, ssp_admin_user, ssp_admin_password):
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

def create_engine(ssp_cm_url, session_token, ssp_engine_description, ssp_engine_host, ssp_engine_name):
    """
    Create an engine on the SSP using the provided session token.
    """
    engine_url = f"https://{ssp_cm_url}/sspcmrest/sspcm/rest/engine/createEngine"
    engine_headers = {
        "X-Authentication": session_token,
        "Content-Type": "application/xml"
    }

    xml_body = f"""
    <engineDef>
      <certicomLogging>ERROR</certicomLogging>
      <debugLogging>ERROR</debugLogging>
      <description><![CDATA[{ssp_engine_description}]]></description>
      <enableAuditLogCMRouting>false</enableAuditLogCMRouting>
      <host>{ssp_engine_host}</host>
      <localPSLogging>ERROR</localPSLogging>
      <maverickLogging>ERROR</maverickLogging>
      <name>{ssp_engine_name}</name>
      <port>65535</port>
      <properties>
        <property>
          <name>proxy.host.name.or.ip</name>
          <value>xx.xx.xx.xx</value>
        </property>
      </properties>
      <status></status>
      <userStore>defUserStore</userStore>
    </engineDef>
    """

    engine_response = requests.post(engine_url, headers=engine_headers, data=xml_body, verify=False)
    return engine_response

# Main logic
if __name__ == "__main__":
    # Set variables
    ssp_cm_url = "<ssp_cm_url>"
    ssp_admin_user = "<ssp_admin_user>"
    ssp_admin_password = "<ssp_admin_password>"
    ssp_engine_description = "<ssp_engine_description>"
    ssp_engine_host = "<ssp_engine_host>"
    ssp_engine_name = "<ssp_engine_name>"

    try:
        # Get session token
        session_token = get_session_token(ssp_cm_url, ssp_admin_user, ssp_admin_password)
        print(f"Session Token: {session_token}")

        # Create engine
        engine_response = create_engine(ssp_cm_url, session_token, ssp_engine_description, ssp_engine_host, ssp_engine_name)
        print(f"Response: {engine_response.text}")

    except Exception as e:
        print(e)
