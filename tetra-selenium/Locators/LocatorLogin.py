class LocatorLogin:
    STAGING_USER_LOGIN_URL = 'https://staging.tetrainsights.com/signin'
    NINJA_USER_LOGIN_URL = 'https://app.testing.tetrainsights.ninja/projects'
    TEST_USER_LOGIN_URL = 'https://app.testing.tetrainsights.ninja/signin'
    LOCAL_USER_LOGIN_URL = 'http://localhost:4200/signin'

    # Login Page
    login_user_email = {'css': '[sln-id="sln-email"]'}
    login_user_password = {'css': '[sln-id="sln-password"]'}
    login_user_button_login = {'css': '[sln-id="sln-login-btn"]'}
    login_user_link_forgot_password = {'css': '[sln-id="sln-fpassword"]'}
    login_user_link_create_account = {'css': '[sln-id="sln-register"]'}
    login_message_bad_password = {'css': '[sln-id="sln-notify"]'}
    login_message_bad_values = {'css': '[sln-id] = "sln-invalid-values"'}
    login_notify = {'css': '[sln-id="sln-notify"]'}

    #
    login_mate_accept = {'css': 'body > appcues > cue > div > div > a'}
    login_mate_close = {'css': 'body > appcues > div.appcues - skip > a'}
    login_iframe_track = {'css': 'body > div.appcues > appcues-container > iframe'}
    login_back_sign = {
        'css': '#SIGN-UP > app-tetra-view-container > div > tcl-grid-column > div > aw-wizard > div > '
               'aw-wizard-completion-step > tcl-confirmation-card > tcl-card-container > div > div > div > div > a'}

    login_signup_ok = {'css': '#SIGN-UP'}

    # 2 factor
    login_request_code = {'css': '#requestCode'}
    login_request_submit = {'css': '#submit-request-code-btn'}

