const Payment = require("../models/Payment");

const createPaymentLink = async (phone) => {
  const amount = 999; // your price

  // Dummy payment link (replace later with Razorpay)
  const paymentLink = `https://your-payment-link.com/pay?phone=${phone}`;

  const payment = await Payment.create({
    phone,
    amount,
    paymentLink
  });

  return payment;
};

module.exports = { createPaymentLink };