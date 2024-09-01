
const {app, BrowserWindow} = require("electron");

app.disableHardwareAcceleration();  // Disable hardware acceleration

function ElectronMainMethod() {
    const launchWindow = new BrowserWindow({
        title: "Tipper",
        width: 2000,
        height: 1000
    });

    const appURL = "http://localhost:8000"

    launchWindow.loadURL(appURL);
}

app.whenReady().then(ElectronMainMethod)