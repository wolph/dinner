$.ajaxSetup({
    crossDomain: false,
    beforeSend: function(xhr, settings) {
        if (!(/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type))){
            xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
        }
    }
});

