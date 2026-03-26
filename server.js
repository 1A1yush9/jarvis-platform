const express = require("express");
const bodyParser = require("body-parser");
const { MessagingResponse } = require("twilio").twiml;

const app = express();

// Middleware
app.use(bodyParser.urlencoded({ extended: false }));

// Root route (for testing server)
app.get("/", (req, res) => {
    console.log("Root HIT ✅");
    res.send("Server Working ✅");
});

// Webhook route (Twilio hits here)
app.post("/webhook", (req, res) => {
    console.log("Webhook HIT ✅");
    console.log("From:", req.body.From);
    console.log("Message:", req.body.Body);

    const twiml = new MessagingResponse();

    // Simple auto reply
    twiml.message("🔥 Jarvis LIVE — Auto Reply Working!");

    res.set("Content-Type", "text/xml");
    res.send(twiml.toString());
});

// Start server
const PORT = process.env.PORT || 10000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});