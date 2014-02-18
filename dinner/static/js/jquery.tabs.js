(function($, window, document, undefined){

var Tabs = function(elem, options){
    this.elem = elem;
    this.$elem = $(elem);
    this.options = options;
    this.metadata = this.$elem.data('tabs-options')
}


Tabs.prototype = {
    defaults: {
        activeTabClass: 'active',
        activeButtonClass: 'active',
        tabSelector: 'div.tab-pane',
        buttonSelector: 'ul.nav-tabs li',
        dataProperty: 'tab',
    },
    init: function(){
        this.options = $.extend(true, {}, this.defaults, this.options,
            this.metadata);
        this.tab = this.getActiveTab().data(this.options.dataProperty);
        this.activate();

        return this;
    },
    getTabs: function(){
        return this.$elem.find(this.options.tabSelector);
    },
    getButtons: function(){
        return this.$elem.find(this.options.buttonSelector);
    },
    getActiveTab: function(){
        return this.getTabs().filter('.' + this.options.activeTabClass);
    },
    getActiveButton: function(){
        return this.getButtons().filter('.' + this.options.activeButtonClass);
    },
    getTab: function(tab){
        return this.getTabs().filter(
            '[data-' + this.options.dataProperty + '="' + tab + '"]');
    },
    getButton: function(tab){
        return this.getButtons().filter(
            '[data-' + this.options.dataProperty + '="' + tab + '"]');
    },
    activate: function(){
        /* Support both with and without event */
        var tab = this.tab;
        if(arguments.length)tab = arguments[arguments.length - 1];

        /* Make sure we set the current tab for the next call */
        this.tab = tab;

        /* Remove the active class from the button and tab to hide it */
        this.getActiveTab().removeClass(this.options.activeTabClass);
        this.getActiveButton().removeClass(this.options.activeButtonClass);

        /* Add the active class to show the new button and tab */
        this.getTab(tab).addClass(this.options.activeTabClass);
        this.getButton(tab).addClass(this.options.activeButtonClass);

        /* Cancel whatever event was linked to this */
        return false;
    },
};

$.fn.tabs = function(options){
    return (new Tabs(this, options).init());
};

})(jQuery, window, document);
