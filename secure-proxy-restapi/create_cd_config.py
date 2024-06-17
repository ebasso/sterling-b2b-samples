import requests
import json
import re

# Function to get session token
def get_session_token(ssp_cm_url, ssp_admin_user, ssp_admin_password):
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
        match = re.search(r'"sessionToken":"([a-zA-Z0-9+/=]+)"', session_response.text)
        if match:
            session_token = match.group(1)
            return session_token
        else:
            raise Exception("Session token not found in the response")
    else:
        raise Exception(f"Failed to get session token: {session_response.text}")

# Function to create CD Policy
def create_cd_policy(ssp_cm_url, session_token, cd_policy_name):
    cd_policy_url = f"https://{ssp_cm_url}/sspcmrest/sspcm/rest/policy/createPolicy"
    cd_policy_headers = {
        "X-Authentication": session_token,
        "Content-Type": "application/xml"
    }

    xml_body = f"""
    <cdPolicyDef>
      <copyStepAllowed>true</copyStepAllowed>
      <eaCertValidation>false</eaCertValidation>
      <ipAddressCheck>true</ipAddressCheck>
      <name>{cd_policy_name}</name>
      <protocol>cd</protocol>
      <protocolErrorAction>NONE</protocolErrorAction>
      <protocolValidationOn>true</protocolValidationOn>
      <runJobStepAllowed>true</runJobStepAllowed>
      <runTaskStepAllowed>true</runTaskStepAllowed>
      <status></status>
      <submitStepAllowed>true</submitStepAllowed>
      <userAuthentication>none</userAuthentication>
      <userMapping>noUserID</userMapping>
    </cdPolicyDef>
    """

    cd_policy_response = requests.post(cd_policy_url, headers=cd_policy_headers, data=xml_body, verify=False)
    return cd_policy_response

# Function to create CD Netmap
def create_cd_netmap(ssp_cm_url, session_token, cd_netmap_name, cd_policy_name):
    cd_netmap_url = f"https://{ssp_cm_url}/sspcmrest/sspcm/rest/netmap/createNetmap"
    cd_netmap_headers = {
        "X-Authentication": session_token,
        "Content-Type": "application/xml"
    }

    xml_body = f"""
    <netmapDef>
      <description>Connect_Direct_Netmap</description>
      <inboundNodes>
        <inboundNodeDef>
          <addresses>
            <address>
              <nodeName>ccenterdev03.irv.ustx.ibm.com</nodeName>
              <host>ccenterdev03.irv.ustx.ibm.com</host>
              <port>4163</port>
            </address>
          </addresses>
          <description>ccenterdev03.irv.ustx.ibm.com</description>
          <logLevel>NONE</logLevel>
          <name>ccenterdev03.irv.ustx.ibm.com</name>
          <outboundACLNodes>
            <outboundACLNode>ccenterdev03.irv.ustx.ibm.com</outboundACLNode>
          </outboundACLNodes>
          <peerAddressPattern>ccenterdev03.irv.ustx.ibm.com</peerAddressPattern>
          <policyId>{cd_policy_name}</policyId>
          <port>4163</port>
          <routingName>ccenterdev03.irv.ustx.ibm.com</routingName>
          <secureConnection>false</secureConnection>
          <serverAddress>ccenterdev03.irv.ustx.ibm.com</serverAddress>
          <tcpTimeout>90</tcpTimeout>
        </inboundNodeDef>
      </inboundNodes>
      <name>{cd_netmap_name}</name>
      <outboundACLRequired>false</outboundACLRequired>
      <protocol>cd</protocol>
      <status></status>
    </netmapDef>
    """

    cd_netmap_response = requests.post(cd_netmap_url, headers=cd_netmap_headers, data=xml_body, verify=False)
    return cd_netmap_response

# Function to create CD Adapter
def create_cd_adapter(ssp_cm_url, session_token, cd_adapter_name, cd_netmap_name):
    cd_map_url = f"https://{ssp_cm_url}/sspcmrest/sspcm/rest/adapter/createAdapter"
    cd_map_headers = {
        "X-Authentication": session_token,
        "Content-Type": "application/xml"
    }

    xml_body = f"""
    <cdAdapterDef>
        <encryptionLevel>false</encryptionLevel>
        <engines></engines>
        <faspPortrange>1000-2000</faspPortrange>
        <listenPort>25000</listenPort>
        <logLevel>DEBUG</logLevel>
        <maxSessions>20</maxSessions>
        <name>{cd_adapter_name}</name>
        <netmap>{cd_netmap_name}</netmap>
        <netmapKey>ccenterdev03.irv.ustx.ibm.com</netmapKey>
        <properties></properties>
        <protocol>cd</protocol>
        <sessionTimeout>90</sessionTimeout>
        <standardRoute>ccenterdev03.irv.ustx.ibm.com</standardRoute>
        <status></status>
        <urlRoutingType>standardRouting</urlRoutingType>
    </cdAdapterDef>
    """

    cd_map_response = requests.post(cd_map_url, headers=cd_map_headers, data=xml_body, verify=False)
    return cd_map_response

# Main logic
if __name__ == "__main__":
    try:
        # Set SSP connection details
        ssp_cm_url = "<ssp_cm_url>"
        ssp_admin_user = "<ssp_admin_user>"
        ssp_admin_password = "<ssp_admin_password>"

        # Get session token
        session_token = get_session_token(ssp_cm_url, ssp_admin_user, ssp_admin_password)
        print(f"Session Token: {session_token}")

        # Create CD Policy
        cd_policy_name = "<cd_policy_name>"
        cd_policy_response = create_cd_policy(ssp_cm_url, session_token, cd_policy_name)
        print(f"CD Policy Response: {cd_policy_response.text}")

        # Create CD Netmap
        cd_netmap_name = "<cd_netmap_name>"
        cd_netmap_response = create_cd_netmap(ssp_cm_url, session_token, cd_netmap_name, cd_policy_name)
        print(f"CD Netmap Response: {cd_netmap_response.text}")

        # Create CD Map
        cd_adapter_name = "<cd_adapter_name>"
        cd_map_response = create_cd_adapter(ssp_cm_url, session_token, cd_adapter_name, cd_netmap_name)
        print(f"CD Adapter Response: {cd_map_response.text}")

    except Exception as e:
        print(e)
