var wol = require("wake_on_lan");
const { serverMac } = require("./config.json")

wol.wake(serverMac);