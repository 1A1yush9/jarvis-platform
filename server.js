require("dotenv").config();
const express = require("express");
const cors = require("cors");

const connectDB = require("./config/db");

const publicRoutes = require("./routes/publicRoutes");
const protectedRoutes = require("./routes/protectedRoutes");
const webhookRoutes = require("./routes/webhookRoutes");

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// DB Connection
connectDB();

// Routes
app.use("/api/public", publicRoutes);
app.use("/api/protected", protectedRoutes);
app.use("/webhook", webhookRoutes);

// Health check
app.get("/", (req, res) => {
  res.send("Jarvis SaaS Backend Running ✅");
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));