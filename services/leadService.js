const Lead = require("../models/Lead");

const createOrUpdateLead = async (phone, message) => {
  let lead = await Lead.findOne({ phone });

  if (!lead) {
    lead = await Lead.create({
      phone,
      name: "WhatsApp Lead"
    });
  }

  lead.messages.push({
    text: message,
    from: "user",
    time: new Date()
  });

  await lead.save();
  return lead;
};

const updateLeadData = async (lead, intentData) => {
  lead.intent = intentData.intent;
  lead.score = intentData.score;

  if (intentData.score >= 8) {
    lead.stage = "ready_to_buy";
  } else if (intentData.score >= 5) {
    lead.stage = "interested";
  } else {
    lead.stage = "new";
  }

  await lead.save();
};

module.exports = { createOrUpdateLead, updateLeadData };