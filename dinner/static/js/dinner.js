jQuery(function($){
    var form = $('form#dinner_signup');
    var visible_inputs =  form.find(':input:visible');
    var tabs = $('#signup_tabs').tabs({dataProperty: 'date'});
    History.Adapter.bind(window, 'statechange', function(e){
        $('form').attr('action', document.location.pathname);
        tabs.activate(History.getState().data.tab);
    });

    /* Restore the state from localStorage if available */
    var state = localStorage.getItem(STATE_KEY)
    if(state)
        form.unserializeForm(state, {'override-values': true});

    /* Save the form state (name, email, etc...) to localStorage */
    function saveState(){
        localStorage.setItem(STATE_KEY, visible_inputs.serialize());
    }
    visible_inputs
        .on('keyup', saveState)
        .on('change', saveState);

    /* Making sure our tabs work with the browser history */
    $('#signup_tabs').on('click', 'li[data-date]', function(e){
        /* Change the url so reloads work :) */
        var tab = $(this).data('date');
        History.pushState({tab: tab}, null, BASE_URL + tab + '/');
        return false;
    });

    /* Submit the forms with ajax */
    $('#courses, #signup_tabs').on('click', 'button.btn', function(e){
        var $this = $(this);
        if(!$this.data('skip-validation') && !form.parsley('validate'))
            return false;

        /* Switch to the right tab */
        var tab = $this.data('date');
        if(tab){
        History.pushState({tab: tab}, null, BASE_URL + tab + '/');
        }

        /* Set the button to the loading state */
        $this.button('loading');

        $.ajax({
            url: document.location.href,
            type: 'POST',
            data: $.extend(
                form.serializeArray(),
                [{name: $this.attr('name'), value: $this.val()}]
            ),
            success: function(data){
                $('div#signup_tabs div.tabs-container').html(
                    $(data).find('div#signup_tabs div.tabs-container').children());
                $this.button('reset');
                tabs.activate();
            },
            dataType: 'html'
        });
        return false;
    });
});

