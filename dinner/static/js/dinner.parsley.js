$.extend($.fn.parsley.defaults, {
  // basic data-api overridable properties here..
  inputs: 'input, textarea, select'           // Default supported inputs.
  , excluded: 'input[type=hidden], :disabled' // Do not validate input[type=hidden] & :disabled.
  , trigger: 'keyup change focusin focusout'  // $.Event() that will trigger validation. eg: keyup, change..
  , animate: false                            // fade in / fade out error messages
  , focus: 'first'                            // 'fist'|'last'|'none' which error field would have focus first on form validation
  , validationMinlength: 0                    // If trigger validation specified, only if value.length > validationMinlength
  , successClass: 'has-success'           // Class name on each valid input
  , errorClass: 'has-error'               // Class name on each invalid input
  , errorMessage: false                       // Customize an unique error message showed if one constraint fails
  , validators: {}                            // Add your custom validators functions
  , showErrors: true                          // Set to false if you don't want Parsley to display error messages
  , messages: {}                              // Add your own error messages here
 
  //some quite advanced configuration here..
  , validateIfUnchanged: true                 // false: validate once by field value change
  , errors: $.extend($.fn.parsley.defaults.errors, {
      classHandler: function ( elem, isRadioOrCheckbox ) {
        // specify where parsley error-success classes are set
        return $(elem).parents(".form-group");
      }
    , container: function ( elem, isRadioOrCheckbox ) {}
    , errorsWrapper: '<span class="help-block"></span>'                                        // do not set an id for this elem, it would have an auto-generated id
    , errorElem: '<p></p>'                                            // each field constraint fail in an li
  })
  , listeners: $.extend($.fn.parsley.defaults.listeners, {
      onFieldValidate: function ( elem, ParsleyForm ) { return false; } // Executed on validation. Return true to ignore field validation
    , onFormSubmit: function ( isFormValid, event, ParsleyForm ) {}     // Executed once on form validation
    , onFieldError: function ( elem, constraints, ParsleyField ) {}     // Executed when a field is detected as invalid
    , onFieldSuccess: function ( elem, constraints, ParsleyField ) {}   // Executed when a field passes validation
  })
});

/* Activate parsley on every blur of every input element */
$('input').focusout(function(){$(this).parsley('validate')});
