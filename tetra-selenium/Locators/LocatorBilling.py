class LocatorBilling:
    billing_plan_basic = {'css': '#BILLING > app-tetra-view-container > div > app-tetra-grid-column > div > div > '
                                 'div > div > div > div > div > div > div:nth-child(2) > div'}
    billing_plan_premium = {'css': '#BILLING > app-tetra-view-container > div > app-tetra-grid-column > div > div '
                                   '> div > div > div > div > div > div > div:nth-child(3) > div'}
    billing_plan_enterprise = {'css': '#BILLING > app-tetra-view-container > div > app-tetra-grid-column > div '
                                      '> div > div > div > div > div > div > div > div:nth-child(4) > div'}
    billing_tab_methods = {
        'css': '#BILLING > app-tetra-view-container > div > app-tetra-grid-column > div > div > div > div > ul > '
               'li:nth-child(2)'}
    billing_contact_us_button = {'css': '#contactForEnterprise-btn > button > a'}
    billing_input_card = {
        'css': '#app > div > div:nth-child(2) > div > div >div:nth-child(2) > div > div > div > div > div:nth-child('
               '2) > div:nth-child(1)'}
    billing_cancel_error_number = {
        'css': '#cb-body > div.cb-modal.cb-modal--overlay > div > div.cb-modal__actions > div > button > span'}
    billing_add_button = {'css': 'button[data-cb-id="card_payment_submit"]'}
    billing_frame_pay = {'css': '#intercom-frame'}
    billing_primary_span = {
        'css': '#cb-body > div > div.cb-body__content > div.cb-section.cb-bar > div > div > div > div > div > span'}
    billing_plan_details = {
        'css': '#BILLING > app-tetra-view-container > div > app-tetra-grid-column > div > div > div > div > div > div '
               '> div > div > div.col-2 > tcl-button > button > a'}
    billing_update_premium = {'css': '#upgradeToPremium-btn > button > span'}
    billing_mem_plan = {
        'css': '#BILLING > app-tetra-view-container > div > app-tetra-grid-column > div > div > div > div > ul > '
               'li:nth-child(1) > h2'}
    billing_purchase_order = {'css': '#upgradeToPremium-btn > button > span'}
    billing_txt_upgraded = {'css': '#generic-template-modal > div.modal-header > h5'}
    billing_back = {'css': '#submit-genericModal-btn > button > span'}
    billing_number = {'css': '#cb-body > div > div >div >div > div > div> div> div> input'}
    billing_month = {'css': '#exp_month'}
    billing_year = {'css': '#exp_year'}
    billing_cvv = {'css': '#cvv'}
    billing_update_problem = {'css': '#submit-genericModal-btn > button > span'}
    login_back_problem_order = {'css': '#goBackToBilling-btn > button'}

