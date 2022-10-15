class LocatorLeftMenu:
    # Left Menu
    nav_menu = {'css': '#DYNAMIC_SIDE_NAV'}
    invite_teammate = {
        'css': '#DYNAMIC_SIDE_NAV > div.sidebar-wrapper.p-1.pretty-scrollbar.ng-tns-c250-0 > '
               'ul.nav.flex-column.mb-4.ng-tns-c250-0 > a > tcl-icon > span > i'}
    settings = {'css': '#navbarUserMenu > span'}

class Settings:
    account_settings = {'css': '#navbarUserMenu > div > a:nth-child(2) > tcl-icon > span > span'}
    billing = {'css': '#navbarUserMenu > div > a.dropdown-item.ng-tns-c250-0.ng-star-inserted'}
    logout = {'css': '#navbarUserMenu > div >:last-child'}

class AccountSetting:
    team = {'css': '#team-tab-btn > button > span'}
    new_invite = {
        'css': '#pInv_LpG2CzHEmnJvQDewEeGAA9aW > div > div > div > div.col-12.col-md-4.pl-0.email-field.field > span'}


class InviteTeammate:
    teammate_mail = {
        'css': '#inviteNewTeammates > div.modal-body.pt-0.ng-star-inserted > div:nth-child(1) > div > div.col-7 > '
               'div > input'}
    invite_btn = {'css': '#send-invitation-btn > button > span'}

    invite_rol = {
        'css': '#inviteNewTeammates > div.modal-body.pt-0.ng-star-inserted > div:nth-child(1) > div > div.col-4 > div '
               '> div > div.input-holder > button'}

    rol_collaborator = {
        'css': '#inviteNewTeammates > div.modal-body.pt-0.ng-star-inserted > div:nth-child(1) > div > div.col-4 > div '
               '> div > div:nth-child(2) > a'}
