import "bootstrap";
import Cookies from "js-cookie";

jQuery(function () {

  var themeForm = $("#themeForm");

  themeForm.find('select[name="theme_name"]').val(document.body.getAttribute('data-theme'));
  themeForm.on("submit", function (e) {
    e.preventDefault();

    var form = $(this);
    var url = form.attr("action");

    $.ajax({
      type: "POST",
      url: url,
      data: form.serialize(),
      success: function (data) {
        window.location.reload();
      },
    });
  });
});
