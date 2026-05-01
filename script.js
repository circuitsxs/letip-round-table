const logos = [
  { src: "images/logos/12-volt.png", alt: "12 Volt Solutions", url: "https://www.12voltfleetsolutions.com" },
  { src: "images/logos/barillari-lawfirm.png", alt: "Barillari Law Firm", url: "https://www.injurylawyerstatenisland.com" },
  { src: "images/logos/cross-country.png", alt: "CrossCountry Mortgage", url: "https://crosscountrymortgage.com/morganville-nj-3428/daniel-holton/" },
  { src: "images/logos/data-solutions.png", alt: "Reliable Data USA", url: "https://www.reliabledatausa.com" },
  { src: "images/logos/design-build.png", alt: "Design Build SI", url: "https://db-si.com" },
  { src: "images/logos/deville-auto.png", alt: "DeVille Auto", url: "https://www.devilleauto.com" },
  { src: "images/logos/edward-jones.png", alt: "Edward Jones", url: "https://www.edwardjones.com/cinzia-laurenza" },
  { src: "images/logos/fjc-financial.png", alt: "FJC Financial Group", url: "https://ficfinancial.com" },
  { src: "images/logos/gallucci-lawfirm.png", alt: "Gallucci Law Firm", url: "https://galluccilawfirm.com" },
  { src: "images/logos/gerald-peters.png", alt: "Gerald Peters Jewelers", url: "https://www.geraldpeters.com" },
  { src: "images/logos/manhattan-electrical.png", alt: "Manhattan Electrical", url: "https://network.procore.com/p/manhattan-electric-supply-staten-island" },
  { src: "images/logos/matt-woitkowsi.png", alt: "Woitkowski Law", url: "https://woitkowski.law" },
  { src: "images/logos/northfield-bank.png", alt: "Northfield Bank", url: "https://www.enorthfield.com" },
  { src: "images/logos/precious-properties.png", alt: "Precious Properties", url: "https://www.preciousproperties.com" },
  { src: "images/logos/qualitech-computers.png", alt: "Qualitech Computers", url: "https://www.qualitechcomputers.com" },
  { src: "images/logos/taranto-construction.png", alt: "Taranto Construction", url: "https://www.tarantoconst.com" },
  { src: "images/logos/world-insurance.png", alt: "World Insurance", url: "https://www.worldinsurance.com" }
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

  if (logo) {
    item.innerHTML = `
      <a href="${logo.url}">
        <img src="${logo.src}" alt="${logo.alt}">
      </a>
    `;
  }
});


const resourceTabs = document.querySelectorAll(".resource-tab");
const resourcePanels = document.querySelectorAll(".resource-panel");

resourceTabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    const targetId = tab.dataset.resource;

    resourceTabs.forEach((button) => {
      button.classList.remove("active");
    });

    resourcePanels.forEach((panel) => {
      panel.classList.remove("active");
    });

    tab.classList.add("active");
    document.getElementById(targetId).classList.add("active");
  });
});