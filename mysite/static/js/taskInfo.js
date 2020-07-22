function showTaskInfo(parameters) {
    $('#taskModal .modal-title').html(parameters.title);
    $('#taskModal .author').html("@" + parameters.author);
    $('#taskModal .pub_date').html(parameters.pub_date);
    $('#taskModal .lead_time').html("до " + parameters.lead_time);
    $('#taskModal .edit').attr("href", "tasks/edit_task/" + parameters.work_id);
    $('#taskModal .delete').attr("href", "tasks/delete_task/" + parameters.work_id);
    $('#taskModal').modal('show');
}