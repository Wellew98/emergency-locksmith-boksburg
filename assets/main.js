document.addEventListener("DOMContentLoaded", function () {
  var l = document.getElementById("navlinks");
  var t = document.querySelector(".nav__toggle");
  if (t && l) {
    t.addEventListener("click", function () {
      var open = l.classList.toggle("open");
      t.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  if (l) {
    l.addEventListener("click", function (e) {
      if (e.target.tagName === "A" && innerWidth <= 900) {
        l.classList.remove("open");
        if (t) t.setAttribute("aria-expanded", "false");
      }
    });
  }
});
