function openEditModal(id) {
     var link = '/admin/'+ id +'/get_user';
     $("#editAcct").load(link);
     $("#editAcct").modal('show');
}

function loadTable(){
     var link = '/admin/1' +'/get_all_users';
      $("#userDataTable").load(link, function() {
                  $('#dataTable').dataTable({
                     "sPaginationType": "full_numbers"
                  });
      });
};
