const Razorpay = require("razorpay");
const crypto = require("crypto");
const Payment = require("../models/Payment");
const User = require("../models/User");

const razorpay = new Razorpay({
  key_id: process.env.RAZORPAY_KEY_ID,
  key_secret: process.env.RAZORPAY_KEY_SECRET
});

// ✅ CREATE ORDER
exports.createOrder = async (req, res) => {
  try {
    const options = {
      amount: 49900,
      currency: "INR",
      receipt: "order_" + Date.now()
    };

    const order = await razorpay.orders.create(options);

    await Payment.create({
      userId: req.user.id,
      razorpay_order_id: order.id,
      amount: options.amount
    });

    res.json(order);

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Order creation failed" });
  }
};

// ✅ VERIFY PAYMENT (SECURE)
exports.verifyPayment = async (req, res) => {
  try {
    const {
      razorpay_order_id,
      razorpay_payment_id,
      razorpay_signature
    } = req.body;

    const body = razorpay_order_id + "|" + razorpay_payment_id;

    const expectedSignature = crypto
      .createHmac("sha256", process.env.RAZORPAY_KEY_SECRET)
      .update(body)
      .digest("hex");

    if (expectedSignature !== razorpay_signature) {
      return res.status(400).json({ success: false });
    }

    // ✅ Secure update (user-specific)
    const payment = await Payment.findOneAndUpdate(
      {
        razorpay_order_id,
        userId: req.user.id
      },
      {
        razorpay_payment_id,
        status: "paid",
        paidAt: new Date()
      },
      { new: true }
    );

    if (!payment) {
      return res.status(404).json({ error: "Payment not found" });
    }

    // ✅ Upgrade user
    await User.findByIdAndUpdate(req.user.id, {
      plan: "pro"
    });

    res.json({ success: true });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Verification failed" });
  }
};