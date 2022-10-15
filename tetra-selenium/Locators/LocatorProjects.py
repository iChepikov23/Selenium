class LocatorProjects:
    projects_table_empty = {'css': 'h4[class ="empty-table-list ng-star-inserted"]'}
    projects_create_project = {'css': '#create-project-btn > button'}
    projects_name_project = {'css': '#create-project-modal > div.modal-body.p-0 > form > app-project-name-input > div '
                                    '> input'}
    projects_desc_project = {'css': '#create-project-description-input'}

    project_select_public = {'css': '#create-project-modal > div.modal-body.p-0 > form > app-project-access > div > '
                                    'div.d-flex.ng-untouched.ng-pristine.ng-invalid > '
                                    'button'}
    project_select_private = {
        'css': '#create-project-modal > div.modal-body.p-0 > form > app-project-access > div > '
               'div.d-flex.ng-untouched.ng-pristine.ng-valid > button:nth-child(3)'}

    project_select_private_on_create = {
        'css': '#create-project-modal > div.modal-body.p-0 > form > app-project-access > div > '
               'div.d-flex.ng-dirty.ng-valid.ng-touched > button:nth-child(3)'}

    project_create_button = {'css': '#createProjectModal-create-btn > button'}

    project_create_notify = {
        'css': '#notify > div > div > div.col-10.col-md-9.col-sm-8.d-flex > span.notify-label.mr-2'}

    project_options = {'css': '#undefined > tcl-icon > span > i'}

    project_delete = {
        'css': '#project-table > div > ngx-datatable > div > datatable-body > datatable-selection > '
               'datatable-scroller > datatable-row-wrapper > datatable-body-row > '
               'div.datatable-row-center.datatable-row-group.ng-star-inserted > datatable-body-cell:nth-child(5) > '
               'div > app-tetra-table-cell > td > span > app-table-common-contextual-menu > app-contextual-dropdown > '
               'div > div > app-contextual-dropdown-item:nth-child(3) > a > tcl-icon > span > span'}

    project_delete_confirm = {
        'css': '#delete-confirmation-modal > div.modal-footer.d-flex.modal-footer-alt > tcl-button:nth-child(1) > '
               'button'}

    project_edit = {
        'css': '#project-table > div > ngx-datatable > div > datatable-body > datatable-selection > '
               'datatable-scroller > datatable-row-wrapper > datatable-body-row > '
               'div.datatable-row-center.datatable-row-group.ng-star-inserted > datatable-body-cell:nth-child(5) > '
               'div > app-tetra-table-cell > td > span > app-table-common-contextual-menu > app-contextual-dropdown > '
               'div > div > app-contextual-dropdown-item:nth-child(2) > a'}

    project_names = {'css': '#project-table > div > ngx-datatable > div > datatable-body > datatable-selection > '
                            'datatable-scroller > :nth-child($number) > datatable-body-row > '
                            'div.datatable-row-center.datatable-row-group.ng-star-inserted > '
                            'datatable-body-cell:nth-child(1) > div > app-tetra-table-cell > td > span > a'}

    project_update = {'css': '#createProjectModal-create-btn > button > span'}

    project_search = {'css': '#search-box-header'}

    project_table_container = {
        'css': '#project-table > div > ngx-datatable > div > datatable-body > datatable-selection > datatable-scroller'}

    project_rows = {'css': '#project-table > div > ngx-datatable > div > datatable-body > datatable-selection > '
                           'datatable-scroller>datatable-row-wrapper'}

    project_first_rows_name_project = {
        'css': '.datatable-body-row > div.datatable-row-center.datatable-row-group.ng-star'
               '-inserted > datatable-body-cell:nth-child(1) > div > app-tetra-table-cell > '
               'td > span > a'}

    project_edit_add_teammates = {'css': '#create-project-modal > div.modal-body.p-0 > form > '
                                         'app-project-add-teammates > div > angular2-multiselect > div > '
                                         'div.selected-list > div > span:nth-child(1)'}

    project_add_first_teammate = {'css': '#create-project-modal > div.modal-body.p-0 > form > '
                                         'app-project-add-teammates > div > angular2-multiselect > div > '
                                         'div.dropdown-list.animated.fadeIn.dropdown-list-top > div.list-area > '
                                         'div:nth-child(3) > ul > li:nth-child(1) > div > '
                                         'label.mr-2.multi-select-username'}

    project_info = {
        'css': '#PROJECT_DASHBOARD_CONTAINER > app-tetra-view-container > div > app-tetra-grid-column:nth-child(2) > '
               'div > app-metrics-holder > div > div'}
