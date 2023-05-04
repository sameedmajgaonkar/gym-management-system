const observer = new IntersectionObserver((enteries) => {
  enteries.forEach((entry) => {
    console.log(entry);
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    } else {
      entry.target.classList.remove("show");
    }
  });
});

const hidden = document.querySelectorAll(".hidden");

hidden.forEach((el) => observer.observe(el));
