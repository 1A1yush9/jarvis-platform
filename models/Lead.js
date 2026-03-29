const mongoose = require("mongoose");

const LeadSchema = new mongoose.Schema({
  phone: String,
  message: String,
  response: String,
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User"
  }
}, { timestamps: true });

module.exports = mongoose.model("Lead", LeadSchema);