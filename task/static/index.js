$(function() {
  var $formEdit = $('.edit-form');
  var $comment = $formEdit.find('[name="comment"]');
  var $agreedElems = $formEdit.find('[name="agreed"]');

  function clearErrors() {
    $formEdit.find('input, textarea').removeClass('is-invalid');
  }

  function noErrors() {
    return $formEdit.find('.is-invalid').length === 0;
  }

  $formEdit.on('submit', function(event) {
    clearErrors()

    var commentVal = $comment.val();
    var agreedVal = $formEdit.find('[name="agreed"]:checked').val();

    if (agreedVal === undefined) {
      $agreedElems.addClass('is-invalid');
    } else if (agreedVal === 'no') {
      if (!commentVal) {
        $comment.addClass('is-invalid');
      }
    }

    if (!noErrors()) {
      event.preventDefault();
    }
  });
});