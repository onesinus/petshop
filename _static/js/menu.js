const sidenav = document.getElementById("sidenav-1");
const instance = mdb.Sidenav.getInstance(sidenav);

let innerWidth = null;

const setMode = (e) => {
    // Check necessary for Android devices
    if (window.innerWidth === innerWidth) {
        return;
    }

    innerWidth = window.innerWidth;

    if (window.innerWidth < 1400) {
        instance.changeMode("over");
        instance.hide();
    } else {
        instance.changeMode("side");
        instance.show();
    }
};

setMode();
window.addEventListener("resize", setMode);