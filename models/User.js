const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  plan: {
    type: String,
    default: "free"
  }
}, { timestamps: true });

module.exports = mongoose.model("User", UserSchema);