const express = require("express");
const bodyParser = require("body-parser");
const { MessagingResponse } = require("twilio").twiml;

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

app.get("/", (req, res) => {
    console.log("Root HIT ✅");
    res.send("Server Working ✅");
});

app.post("/webhook", (req, res) => {
    console.log("Webhook HIT ✅");
    console.log("From:", req.body.From);
    console.log("Message:", req.body.Body);

    const twiml = new MessagingResponse();
    twiml.message("🔥 Jarvis LIVE — Auto Reply Working!");

    res.set("Content-Type", "text/xml");
    res.send(twiml.toString());
});

const PORT = process.env.PORT || 10000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});