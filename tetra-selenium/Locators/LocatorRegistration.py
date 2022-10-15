class LocatorRegistration:
    REGISTRATION_USER_URL = 'https://staging.tetrainsights.com/signin'
    registration_user_tetra_icon = {'css': '#DYNAMIC_TOP_NAV > div.logo.pt-1.pb-1 > a > tcl-logo > img'}
    create_account_locator = {'css': 'a[href="/register"]'}
    registration_user_email = {'css': '#email'}
    registration_user_button_next = {'css': '#check-email-btn > button'}
    registration_user_fullname = {'css': '#fullname'}
    registration_user_name = {'css': '#displayName'}
    registration_user_organization = {'css': '#organization'}
    registration_user_password = {'css': '#password'}
    registration_user_button_sign_up = {'css': '#submit-register-btn > button'}
    registration_user_ok = {
        'css': '#SIGN-UP > app-tetra-view-container > div > tcl-grid-column > div > aw-wizard > div > '
               'aw-wizard-completion-step > tcl-confirmation-card > tcl-card-container > div > div > h4'}

    registration_user_invitation_button_sign_up = {'css': '#submit-register-btn > button'}

    registration_user_error_duplicate = {'css': r"#abId0\.20913582043240586 > app-message-bubble > div"}

    registration_user_msg_duplicate_organization = {'css': '#SIGN-UP > app-tetra-view-container > div > '
                                                           'tcl-grid-column > div > aw-wizard > div > aw-wizard-step > '
                                                           'tcl-card-container > div > div > app-sign-up-form > '
                                                           'app-tetra-grid-row > div > div > form > div:nth-child(3) > '
                                                           'app-message-bubble > div'}

    registration_user_msg_bad_password = {'css': '#REGISTER > div > div > div > div > form > aw-wizard > div > '
                                                 'aw-wizard-completion-step > div:nth-child(5) > app-message-bubble >'
                                                 ' div'}
    registration_terms_conditions = {'css': '#SIGN-UP > app-tetra-view-container > div > tcl-grid-column > div > '
                                            'aw-wizard > div > aw-wizard-step > tcl-card-container > div > div > '
                                            'app-sign-up-form > app-tetra-grid-row > div > div > form > '
                                            'div.row.tetra-card-footer > div > p > a:nth-child(1)'}

    registration_privacy_policy = {'css': '#SIGN-UP > app-tetra-view-container > div > tcl-grid-column > div > '
                                          'aw-wizard > div > aw-wizard-step > tcl-card-container > div > div > '
                                          'app-sign-up-form > app-tetra-grid-row > div > div > form > '
                                          'div.row.tetra-card-footer > div > p > a:nth-child(2)'}

    registration_confirm_mail_text = {'css': '#REGISTER-EMAIL > app-tetra-view-container > div > tcl-grid-column > '
                                             'div > tcl-card-container > div > div'}
