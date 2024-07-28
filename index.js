
const {app, BrowserWindow} = require("electron");

function ElectronMainMethod(){
    const launchWindow = new BrowserWindow({
        title: "realtorhub",
        width: 900,
        height: 800
    });

    const appURL = "http://localhost:8000";

    launchWindow.loadURL(appURL);
}// end main()

app.whenReady().then(ElectronMainMethod)