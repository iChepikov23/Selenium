def get_page_object(driver, page_name):
    test_obj = None
    page_name = page_name.lower()

    if page_name == "billing":
        from Pages.PageBilling import PageBilling
        test_obj = PageBilling(driver)
    elif page_name == "leftmenu":
        from Pages.PageLeftMenu import PageLeftMenu
        test_obj = PageLeftMenu(driver)
    elif page_name == "setting":
        from Pages.PageSetting import PageSetting
        test_obj = PageSetting(driver)
    elif page_name == "teammate":
        from Pages.PageTeammate import PageTeammate
        test_obj = PageTeammate(driver)
    elif page_name == "registration":
        from Pages.PageRegistration import PageRegistration
        test_obj = PageRegistration(driver)
    elif page_name == "login":
        from Pages.PageLogin import PageLogin
        test_obj = PageLogin(driver)
    elif page_name == "projects":
        from Pages.PageProjects import PageProjects
        test_obj = PageProjects(driver)
    return test_obj
