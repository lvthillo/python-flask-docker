import google_auth_oauthlib.flow

CLIENT_CONFIG = {
    "web": {
        "client_id": "143609494029-265o0l4se1kn1c3akjpt07f6j26fh5rd.apps.googleusercontent.com",
        "project_id": "sanbeacon-1161",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        # TODO: need to store secret in other places
        "client_secret": "",
        "redirect_uris": [
            # TODO: redirect URL need to be configured
            "http://localhost:8080"
        ]
    }
}

SCOPES = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/youtube'
]


def get_oauth_redirect_url(direct_uri):
    """
    :param direct_uri:
    :return: authorization_url, state
    """

    # Use the client_secret.json file to identify the application requesting
    # authorization. The client ID (from that file) and access scopes are required.
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=SCOPES)

    # Indicate where the API server will redirect the user after the user completes
    # the authorization flow. The redirect URI is required. The value must exactly
    # match one of the authorized redirect URIs for the OAuth 2.0 client, which you
    # configured in the API Console. If this value doesn't match an authorized URI,
    # you will get a 'redirect_uri_mismatch' error.
    flow.redirect_uri = direct_uri

    # Generate URL for request to Google's OAuth 2.0 server.
    # Use kwargs to set optional request parameters.
    return flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')


def fetch_access_refresh_token(
        authorization_url,
        flask_session_state,
        call_back_url
):
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=SCOPES,
        state=flask_session_state
    )

    flow.redirect_uri = call_back_url
    flow.fetch_token(authorization_response=authorization_url)

    return flow.credentials

