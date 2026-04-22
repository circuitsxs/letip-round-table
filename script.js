const logos = [
  { src: "images/logos/12-volt.png", alt: "12 Volt Solutions" },
  { src: "images/logos/barillari-lawfirm.png", alt: "Barillari Law Firm" },
  { src: "images/logos/cross-country.png", alt: "CrossCountry Mortgage" },
  { src: "images/logos/data-solutions.png", alt: "DataUSA" },
  { src: "images/logos/design-build.png", alt: "Design Build" },
  { src: "images/logos/deville-auto.png", alt: "DeVille Auto" },
  { src: "images/logos/edward-jones.png", alt: "Edward Jones" },
  { src: "images/logos/fjc-financial.png", alt: "FJC Financial" },
  { src: "images/logos/gallucci-lawfirm.png", alt: "Gallucci Law Firm" },
  { src: "images/logos/gerald-peters.png", alt: "Gerald Peters" },
  { src: "images/logos/manhattan-electrical.png", alt: "Manhattan Electrical" },
  { src: "images/logos/matt-woitkowsi.png", alt: "Woitkowski Law" }, // ⚠️ your file name has a typo
  { src: "images/logos/northfield-bank.png", alt: "Northfield Bank" },
  { src: "images/logos/precious-properties.png", alt: "Precious Properties" },
  { src: "images/logos/qualitech-computers.png", alt: "Qualitech Computers" },
  { src: "images/logos/taranto-construction.png", alt: "Taranto Construction" },
  { src: "images/logos/world-insurance.png", alt: "World Insurance" }
];

function shuffle(array) {
  const copy = [...array];

  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }

  return copy;
}

const selected = shuffle(logos).slice(0, 6);
const items = document.querySelectorAll("#logoGrid .logo-item");

items.forEach((item, index) => {
  const logo = selected[index];
  item.innerHTML = `<img src="${logo.src}" alt="${logo.alt}">`;
});